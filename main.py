"""
E-commerce Analytics API
A FastAPI application providing comprehensive analytics for e-commerce transactions.
"""

from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import JSONResponse
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import Optional, Dict, List, Any
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="E-commerce Analytics API",
    description="Comprehensive analytics API for e-commerce transaction data",
    version="1.0.0"
)

# Global DataFrame to store sales data
sales_df: Optional[pd.DataFrame] = None

def load_sales_data() -> None:
    """
    Load sales data from CSV file with error handling and data type optimization.
    Performs initial data validation and preprocessing for analytics operations.
    """
    global sales_df
    try:
        # Load CSV with optimized data types for performance
        sales_df = pd.read_csv('sales_data.csv')
        
        # Data type optimization
        sales_df['transaction_id'] = sales_df['transaction_id'].astype('category')
        sales_df['product_name'] = sales_df['product_name'].astype('category')
        sales_df['category'] = sales_df['category'].astype('category')
        sales_df['price'] = pd.to_numeric(sales_df['price'], errors='coerce')
        sales_df['quantity'] = pd.to_numeric(sales_df['quantity'], errors='coerce')
        sales_df['customer_age'] = pd.to_numeric(sales_df['customer_age'], errors='coerce')
        sales_df['customer_rating'] = pd.to_numeric(sales_df['customer_rating'], errors='coerce')
        sales_df['revenue'] = pd.to_numeric(sales_df['revenue'], errors='coerce')
        
        # Convert purchase_date to datetime
        sales_df['purchase_date'] = pd.to_datetime(sales_df['purchase_date'])
        
        # Remove any rows with critical missing data
        sales_df = sales_df.dropna(subset=['product_name', 'category', 'price', 'revenue'])
        
        logger.info(f"Successfully loaded {len(sales_df)} records from sales_data.csv")
        
    except FileNotFoundError:
        logger.error("sales_data.csv file not found")
        raise HTTPException(status_code=500, detail="Sales data file not found")
    except Exception as e:
        logger.error(f"Error loading sales data: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error loading sales data: {str(e)}")

def create_error_response(detail: str, status_code: int = 500) -> Dict[str, Any]:
    """
    Create standardized error response format for consistent API error handling.
    
    Args:
        detail: Error description message
        status_code: HTTP status code for the error
        
    Returns:
        Standardized error response dictionary
    """
    return {
        "detail": detail,
        "status_code": status_code,
        "timestamp": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    }

# Load data on startup
@app.on_event("startup")
async def startup_event():
    """Initialize application by loading sales data."""
    load_sales_data()

@app.get("/api/products")
def get_product_list() -> Dict[str, Any]:
    """
    Retrieve basic product list information.
    
    Business Purpose: Provides a simple list of products available in the system.
    
    Returns:
        Basic product list with product names and summary statistics
    """
    try:
        if sales_df is None or sales_df.empty:
            raise HTTPException(status_code=500, detail="No sales data available")
        
        # Get unique products
        unique_products = sales_df['product_name'].unique()
        
        # Build simple product list
        products = []
        for product_name in unique_products:
            products.append({
                "product_name": str(product_name)
            })
        
        # Calculate basic summary metrics
        total_revenue = float(sales_df['revenue'].sum())
        
        return {
            "products": products,
            "total_products": len(products),
            "summary": {
                "total_revenue": round(total_revenue, 2)
            }
        }
        
    except Exception as e:
        logger.error(f"Error in get_product_list: {str(e)}")
        return JSONResponse(
            status_code=500,
            content=create_error_response(f"Error retrieving product data: {str(e)}")
        )

@app.get("/api/categories")
def get_category_performance() -> Dict[str, Any]:
    """
    Analyze category-level performance metrics for strategic category management.
    
    Business Purpose: Enables category managers to optimize product mix, pricing strategies,
    and inventory allocation based on category performance data.
    
    Returns:
        Category performance metrics with revenue distribution and customer satisfaction
    """
    try:
        if sales_df is None or sales_df.empty:
            raise HTTPException(status_code=500, detail="No sales data available")
        
        # Calculate category-level business metrics for strategic analysis
        # Bug 1: Using 'first' instead of 'mean' for average calculations
        category_metrics = sales_df.groupby('category').agg({
            'revenue': ['sum', 'first', 'count'],  # Should be 'mean' not 'first'
            'customer_rating': 'mean',
            'quantity': 'sum'
        }).round(2)
        
        # Flatten multi-level column names for easier access
        category_metrics.columns = ['total_revenue', 'avg_revenue_per_transaction', 'transaction_count', 'avg_rating', 'total_units_sold']
        
        # Bug 2: Using wrong column for total revenue calculation
        total_revenue = float(sales_df['price'].sum())  # Should be 'revenue' not 'price'
        
        # Build category performance report for management
        categories = []
        for category_name, metrics in category_metrics.iterrows():
            # Bug 3: Division by zero not handled properly
            revenue_percentage = (metrics['total_revenue'] / total_revenue * 100)  # Missing zero check
            
            categories.append({
                "category": str(category_name),
                "total_revenue": float(metrics['total_revenue']),
                "avg_revenue_per_transaction": float(metrics['avg_revenue_per_transaction']),
                "transaction_count": int(metrics['transaction_count']),
                "avg_rating": float(metrics['avg_rating']) if pd.notna(metrics['avg_rating']) else None,
                "total_units_sold": int(metrics['total_units_sold']),
                # Bug 4: Using wrong variable name
                "revenue_percentage": round(revenue_percentage, 1)  # Should handle NaN/inf values
            })
        
        # Bug 5: Incorrect calculation - using wrong data
        total_categories = len(sales_df['product_name'].unique())  # Should be category, not product_name
        
        return {
            "categories": categories,
            "total_categories": total_categories
        }
        
    except Exception as e:
        logger.error(f"Error in get_category_performance: {str(e)}")
        return JSONResponse(
            status_code=500,
            content=create_error_response(f"Error analyzing category performance: {str(e)}")
        )

@app.get("/api/revenue-insights")
def generate_revenue_insights() -> Dict[str, Any]:
    """
    Generate comprehensive revenue insights with trends, forecasting, and strategic recommendations.
    
    Business Purpose: Provides executive leadership with advanced analytics for strategic planning,
    revenue optimization, and business growth initiatives.
    
    Returns:
        Advanced revenue analytics including trends, forecasting, and customer segmentation
    """
    try:
        if sales_df is None or sales_df.empty:
            raise HTTPException(status_code=500, detail="No sales data available")
        
        # TODO: Implement actual logic - currently returning placeholder data
        # Candidates need to implement the full logic for this endpoint
        
        return {
            "monthly_trends": [
                {"month": "2024-01", "revenue": 0.0, "transaction_count": 0, "growth_rate": None},
                {"month": "2024-02", "revenue": 0.0, "transaction_count": 0, "growth_rate": 0.0}
            ],
            "top_products": [
                {"product_name": "placeholder", "total_revenue": 0.0, "revenue_contribution": 0.0, "rank": 1},
                {"product_name": "placeholder", "total_revenue": 0.0, "revenue_contribution": 0.0, "rank": 2}
            ],
            "category_distribution": [
                {"category": "placeholder", "revenue": 0.0, "percentage": 0.0}
            ],
            "customer_segments": [
                {"segment": "High Value", "customer_count": 0, "avg_order_value": 0.0, "total_revenue": 0.0, "criteria": "Orders > $200"},
                {"segment": "Medium Value", "customer_count": 0, "avg_order_value": 0.0, "total_revenue": 0.0, "criteria": "Orders $50-$200"},
                {"segment": "Low Value", "customer_count": 0, "avg_order_value": 0.0, "total_revenue": 0.0, "criteria": "Orders < $50"}
            ],
            "growth_metrics": {
                "overall_growth_rate": 0.0,
                "revenue_trend": "insufficient_data",
                "best_performing_month": None,
                "seasonal_pattern": "slight_decline_in_march"
            },
            "forecasting": {
                "predicted_next_month_revenue": 0.0,
                "confidence_level": "medium",
                "key_drivers": ["electronics_sales", "customer_retention"]
            }
        }
        
    except Exception as e:
        logger.error(f"Error in generate_revenue_insights: {str(e)}")
        return JSONResponse(
            status_code=500,
            content=create_error_response(f"Error generating revenue insights: {str(e)}")
        )

# Health check endpoint for monitoring
@app.get("/health")
def health_check():
    """API health check endpoint for monitoring and deployment verification."""
    return {"status": "healthy", "timestamp": datetime.utcnow().isoformat()}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)