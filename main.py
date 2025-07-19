"""
E-commerce Analytics API - Hackathon Challenge
A FastAPI application providing comprehensive analytics for e-commerce transactions.

CHALLENGE INSTRUCTIONS:
1. Implement the /api/get-top-month endpoint to return TOP 5 selling products (currently returns top 3)
2. Complete the /api/categories endpoint implementation (currently incomplete)
3. Debug and fix the /api/demographics endpoint (contains multiple bugs)

Goto line 113 to start working on the first challenge.
Good luck! May the best data scientist win! 🚀
"""

from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
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
    title="E-commerce Analytics API - Hackathon Challenge",
    description="Complete the missing implementations and fix the bugs!",
    version="1.0.0"
)

# Global DataFrame to store sales data
sales_df: Optional[pd.DataFrame] = None

# Pydantic models for request/response validation
class MonthRequest(BaseModel):
    month: str = Field(..., description="Month in YYYY-MM format (e.g., '2024-03')")

class TopProductResponse(BaseModel):
    product_name: str
    revenue: float
    category: str

class TopMonthResponse(BaseModel):
    month: str
    top_products: List[TopProductResponse]
    total_revenue: float

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


# ===============================================================================
# API Endpoints start here
# ===============================================================================
@app.post("/api/get-top-month")
def get_top_selling_products_by_month(request: MonthRequest) -> TopMonthResponse:
    """
    CHALLENGE 1: Modify this endpoint to return TOP 5 selling products instead of top 3
    
    Get the top selling products for a specific month based on revenue.
    
    Business Purpose: Enables product managers to identify best-performing products
    in specific time periods for inventory planning and marketing strategies.
    
    Args:
        request: Request payload containing the month in YYYY-MM format
        
    Returns:
        Top 5 products by revenue for the specified month with their categories
    """
    try:
        if sales_df is None or sales_df.empty:
            raise HTTPException(status_code=500, detail="No sales data available")
        
        # Validate and parse the month format
        try:
            target_date = datetime.strptime(request.month, "%Y-%m")
        except ValueError:
            raise HTTPException(
                status_code=400, 
                detail="Invalid month format. Please use YYYY-MM format (e.g., '2024-03')"
            )
        
        # Filter data for the specified month
        month_data = sales_df[
            (sales_df['purchase_date'].dt.year == target_date.year) &
            (sales_df['purchase_date'].dt.month == target_date.month)
        ]
        
        if month_data.empty:
            raise HTTPException(
                status_code=404, 
                detail=f"No sales data found for month {request.month}"
            )
        
        # Calculate product revenue for the month
        product_revenue = month_data.groupby(['product_name', 'category']).agg({
            'revenue': 'sum'
        }).reset_index()
        top_products = product_revenue.nlargest(5, 'revenue')
        # Calculate total revenue for the month
        total_monthly_revenue = float(month_data['revenue'].sum())
        
        # Build response with top products
        top_products_list = []
        for _, row in top_products.iterrows():
            top_products_list.append(TopProductResponse(
                product_name=str(row['product_name']),
                revenue=float(row['revenue']),
                category=str(row['category'])
            ))
        
        return TopMonthResponse(
            month=request.month,
            top_products=top_products_list,
            total_revenue=round(total_monthly_revenue, 2)
        )
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error in get_top_selling_products_by_month: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Error retrieving top selling products: {str(e)}"
        )

@app.get("/api/categories")
def get_category_performance() -> Dict[str, Any]:
    """
    Analyze category-level performance metrics for strategic category management.
    
    Business Purpose: Enables category managers to optimize product mix, pricing strategies,
    and inventory allocation based on category performance data.
    """
    try:
        if sales_df is None or sales_df.empty:
            raise HTTPException(status_code=500, detail="No sales data available")
        
        # Calculate category-level business metrics for strategic analysis
        category_metrics = sales_df.groupby('category').agg({
            'revenue': ['sum', 'mean', 'count'],  # Revenue metrics
            'customer_rating': 'mean',  # Customer satisfaction
            'quantity': 'sum'  # Units sold
        }).round(2)
        
        # Flatten multi-level column names for easier access
        category_metrics.columns = ['total_revenue', 'avg_revenue_per_transaction', 'transaction_count', 'avg_rating', 'total_units_sold']
        
        # Calculate total revenue for percentage calculations
        total_revenue = float(sales_df['revenue'].sum())
        
        # Build category performance report for management
        categories = []
        for category_name, metrics in category_metrics.iterrows():
            revenue_percentage = (metrics['total_revenue'] / total_revenue * 100) if total_revenue > 0 else 0.0
            
            categories.append({
                "category": str(category_name),
                "total_revenue": float(metrics['total_revenue']),
                "avg_revenue_per_transaction": float(metrics['avg_revenue_per_transaction']),
                "transaction_count": int(metrics['transaction_count']),
                "avg_rating": float(metrics['avg_rating']) if pd.notna(metrics['avg_rating']) else None,
                "total_units_sold": int(metrics['total_units_sold']),
                "revenue_percentage": round(revenue_percentage, 1)
            })
        
        return {
            "categories": categories,
            "total_categories": len(categories)
        }
        
    except Exception as e:
        logger.error(f"Error in get_category_performance: {str(e)}")
        return JSONResponse(
            status_code=500,
            content=create_error_response(f"Error analyzing category performance: {str(e)}")
        )

@app.get("/api/demographics")
def analyze_customer_demographics() -> Dict[str, Any]:
    """
    Perform customer demographic analysis for targeted marketing and customer segmentation.
    
    Business Purpose: Supports marketing teams in developing age-targeted campaigns
    and helps identify high-value customer segments for retention strategies.
    
    Returns:
        Customer demographic breakdown with spending patterns and engagement metrics
    """
    try:
        if sales_df is None or sales_df.empty:
            raise HTTPException(status_code=500, detail="No sales data available")
        
        # Remove rows with missing age data for accurate demographic analysis
        valid_age_data = sales_df.dropna(subset=['customer_age'])
        
        if valid_age_data.empty:
            raise HTTPException(status_code=500, detail="No valid customer age data available")
        
        # Define age groups for marketing segmentation
        def categorize_age(age):
            if age <= 25:
                return "18-25"
            elif age <= 35:
                return "26-35"
            elif age <= 45:
                return "36-45"
            elif age <= 55:
                return "46-55"
            else:
                return "56+"
        
        # Apply age segmentation for demographic analysis
        valid_age_data = valid_age_data.copy()
        valid_age_data['age_group'] = valid_age_data['customer_age'].apply(categorize_age)
        
        # Calculate demographic metrics for marketing intelligence
        demo_metrics = valid_age_data.groupby('age_group').agg({
            'customer_age': 'count',  # Customer count per segment
            'revenue': ['sum', 'mean', 'count'],  # Revenue and spending patterns
            'customer_rating': 'mean'  # Customer satisfaction by age group
        }).round(2)
        
        # Flatten column names for easier processing
        demo_metrics.columns = ['customer_count', 'total_revenue', 'avg_spending', 'transaction_count', 'avg_rating']
        
        # Calculate total revenue for percentage analysis
        total_revenue = float(valid_age_data['revenue'].sum())
        
        # Build demographic analysis for marketing strategy
        age_groups = []
        age_order = ["18-25", "26-35", "36-45", "46-55", "56+"]  # Ordered for reporting
        
        for age_range in age_order:
            if age_range in demo_metrics.index:
                metrics = demo_metrics.loc[age_range]
                revenue_percentage = (metrics['total_revenue'] / total_revenue * 100) if total_revenue > 0 else 0.0
                
                age_groups.append({
                    "age_range": age_range,
                    "customer_count": int(metrics['customer_count']),
                    "avg_spending": float(metrics['avg_spending']),
                    "total_revenue": float(metrics['total_revenue']),
                    "avg_rating": float(metrics['avg_rating']) if pd.notna(metrics['avg_rating']) else None,
                    "transaction_count": int(metrics['transaction_count']),
                    "revenue_percentage": round(revenue_percentage, 1)
                })
        
        # Calculate summary insights for strategic planning
        if not demo_metrics.empty:
            highest_spending_group = demo_metrics['avg_spending'].idxmax()
            largest_group = demo_metrics['customer_count'].idxmax()
            highest_rated_group = demo_metrics['avg_rating'].idxmax() if demo_metrics['avg_rating'].notna().any() else None
            total_customers = int(demo_metrics['customer_count'].sum())
        else:
            highest_spending_group = None
            largest_group = None
            highest_rated_group = None
            total_customers = 0
        
        return {
            "age_groups": age_groups,
            "summary": {
                "total_customers": total_customers,
                "highest_spending_group": str(highest_spending_group) if highest_spending_group else None,
                "largest_group": str(largest_group) if largest_group else None,
                "highest_rated_group": str(highest_rated_group) if highest_rated_group else None
            }
        }
        
    except Exception as e:
        logger.error(f"Error in analyze_customer_demographics: {str(e)}")
        return JSONResponse(
            status_code=500,
            content=create_error_response(f"Error analyzing customer demographics: {str(e)}")
        )



# Health check endpoint for monitoring
@app.get("/health")
def health_check():
    """API health check endpoint for monitoring and deployment verification."""
    return {"status": "healthy", "timestamp": datetime.utcnow().isoformat()}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)