"""
E-commerce Analytics API - Code-a-thon Challenge

Business Context:
This API serves an online retail platform's analytics dashboard, providing insights
into sales performance, customer demographics, and product analytics. The system
processes transaction data to generate business intelligence reports for management
decision-making.

Dataset Description:
The API analyzes 6 months of e-commerce transaction data containing product sales,
customer demographics, and performance metrics. Data includes transactions across
multiple product categories with customer ratings and revenue calculations.

API Purpose:
Provides RESTful endpoints for:
- Product performance analysis
- Sales dashboard summaries
- Category performance metrics
- Customer demographic insights
- Revenue trend analysis
"""

from fastapi import FastAPI, HTTPException, Query
from typing import List, Dict, Any, Optional
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from dateutil import parser
import uvicorn

# Initialize FastAPI application
app = FastAPI(
    title="E-commerce Analytics API",
    description="Analytics API for e-commerce transaction data analysis",
    version="1.0.0"
)

# Global DataFrame for transaction data
df = None

# Data Loading Section
def load_sales_data():
    """
    Load e-commerce sales data from CSV file with error handling
    and data type optimization for performance.
    """
    global df
    try:
        # Load CSV with optimized data types
        df = pd.read_csv('sales_data.csv')
        
        # Convert date column to datetime
        df['purchase_date'] = pd.to_datetime(df['purchase_date'])
        
        # Optimize data types
        df['transaction_id'] = df['transaction_id'].astype('string')
        df['product_name'] = df['product_name'].astype('string')
        df['category'] = df['category'].astype('category')
        df['price'] = df['price'].astype('float32')
        df['quantity'] = df['quantity'].astype('int16')
        df['customer_age'] = df['customer_age'].astype('int16')
        df['customer_rating'] = df['customer_rating'].astype('float32')
        df['revenue'] = df['revenue'].astype('float32')
        
        print(f"Successfully loaded {len(df)} transaction records")
        return True
        
    except FileNotFoundError:
        print("Error: sales_data.csv not found in current directory")
        return False
    except Exception as e:
        print(f"Error loading data: {str(e)}")
        return False

# Load data on startup
if not load_sales_data():
    print("Warning: Could not load sales data. API will return errors.")

# Section 1: Working Enhancement Endpoint
@app.get("/api/products")
def get_product_list():
    """
    Retrieve product performance metrics for inventory management.
    
    Business Purpose: Provides product managers with key performance indicators
    for each product including pricing, sales volume, and revenue contribution.
    
    Current Status: Working but incomplete - missing additional fields and summary
    Enhancement Required: Add average_rating, total_revenue, and summary statistics
    """
    if df is None:
        raise HTTPException(status_code=500, detail="Data not loaded")
    
    try:
        # Current working implementation (incomplete)
        product_metrics = df.groupby('product_name').agg({
            'price': 'mean',
            'quantity': 'sum'
        }).reset_index()
        
        product_metrics.columns = ['product_name', 'price', 'total_count']
        product_metrics['price'] = product_metrics['price'].round(2)
        
        # Convert to list of dictionaries for JSON response
        products = product_metrics.to_dict('records')
        
        return {
            "products": products,
            "total_products": len(products)
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing product data: {str(e)}")

# Section 2: Easy Debug Endpoint
@app.get("/api/dashboard")
def get_dashboard_summary(days: int = Query(30, ge=1, le=180)):
    """
    Generate executive dashboard summary with key business metrics.
    
    Business Purpose: Provides C-suite executives with high-level KPIs
    for strategic decision making and performance monitoring.
    
    Current Status: Broken with obvious bugs in date filtering and aggregation
    """
    if df is None:
        raise HTTPException(status_code=500, detail="Data not loaded")
    
    try:
        # Bug 1: Wrong date filtering logic
        cutoff_date = datetime.now() + timedelta(days=days)  # Should be minus, not plus
        recent_data = df[df['purchase_date'] > cutoff_date]
        
        # Bug 2: Wrong aggregation method for revenue
        total_revenue = recent_data['price'].sum()  # Should use 'revenue' column
        
        # Bug 3: Incorrect calculation for average order value
        avg_order_value = recent_data['quantity'].mean()  # Should be revenue/transaction count
        
        # Bug 4: Wrong column for transaction count
        total_transactions = len(recent_data['product_name'].unique())  # Should be len(recent_data)
        
        # Bug 5: Incorrect rating calculation
        avg_rating = recent_data['customer_rating'].max()  # Should be mean(), not max()
        
        return {
            "period_days": days,
            "total_revenue": round(total_revenue, 2),
            "total_transactions": total_transactions,
            "average_order_value": round(avg_order_value, 2),
            "average_rating": round(avg_rating, 2),
            "data_points": len(recent_data)
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating dashboard: {str(e)}")

# Section 3: Intermediate Debug Endpoint
@app.get("/api/categories")
def get_category_performance():
    """
    Analyze category performance metrics for merchandising decisions.
    
    Business Purpose: Enables merchandising teams to understand category
    performance, optimize inventory allocation, and identify growth opportunities.
    
    Current Status: Broken with complex logic errors in groupby and calculations
    """
    if df is None:
        raise HTTPException(status_code=500, detail="Data not loaded")
    
    try:
        # Bug 1: Incorrect groupby aggregation
        category_stats = df.groupby('category').agg({
            'revenue': ['sum', 'mean', 'count'],
            'customer_rating': 'mean',
            'quantity': 'sum'
        })
        
        # Bug 2: Wrong way to flatten MultiIndex columns
        category_stats.columns = ['_'.join(col).strip() for col in category_stats.columns.values]
        
        # Bug 3: Incorrect percentage calculation
        total_revenue = df['revenue'].sum()
        category_stats['revenue_percentage'] = (category_stats['revenue_sum'] / total_revenue) * 10  # Should be * 100
        
        # Bug 4: Wrong sorting logic
        category_stats = category_stats.sort_values('revenue_mean', ascending=True)  # Should be descending
        
        # Bug 5: Incorrect column renaming
        category_stats = category_stats.rename(columns={
            'revenue_sum': 'total_revenue',
            'revenue_mean': 'avg_revenue_per_transaction',
            'revenue_count': 'transaction_count',
            'customer_rating_mean': 'avg_rating',
            'quantity_sum': 'total_units_sold'
        })
        
        # Bug 6: Missing reset_index()
        results = category_stats.to_dict('records')
        
        return {
            "categories": results,
            "total_categories": len(results)
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error analyzing categories: {str(e)}")

# Section 4: Intermediate Build-from-Scratch
@app.get("/api/demographics")
def analyze_customer_demographics():
    """
    Analyze customer demographics for targeted marketing campaigns.
    
    Business Purpose: Provides marketing teams with customer segmentation insights
    to develop targeted campaigns, personalized offers, and improve customer acquisition.
    
    Requirements:
    - Age group analysis (18-25, 26-35, 36-45, 46-55, 56+)
    - Spending patterns by age group
    - Average ratings by demographic
    - Transaction frequency analysis
    
    Current Status: Empty function - complete implementation needed
    """
    if df is None:
        raise HTTPException(status_code=500, detail="Data not loaded")
    
    try:
        # TODO: Implement customer demographic analysis
        # Hint: Use pd.cut() for age groups
        # Calculate spending patterns, ratings, and transaction counts per group
        
        # Placeholder return - replace with actual implementation
        return {
            "message": "Implementation needed",
            "requirements": [
                "Age group segmentation",
                "Spending analysis by age group",
                "Average ratings by demographic",
                "Transaction frequency by age group"
            ]
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error analyzing demographics: {str(e)}")

# Section 5: Hard Build-from-Scratch
@app.get("/api/revenue-insights")
def generate_revenue_insights():
    """
    Generate comprehensive revenue insights for strategic planning.
    
    Business Purpose: Provides CFO and strategic planning teams with detailed
    revenue analysis including trends, forecasts, and performance indicators
    for budget planning and growth strategy development.
    
    Requirements:
    - Monthly revenue trends over the dataset period
    - Top performing products by revenue contribution
    - Revenue growth rate calculations
    - Seasonal pattern identification
    - Product category revenue distribution
    - Customer value segmentation (high/medium/low value)
    
    Current Status: Empty function - complex analytical implementation needed
    """
    if df is None:
        raise HTTPException(status_code=500, detail="Data not loaded")
    
    try:
        # TODO: Implement comprehensive revenue analysis
        # This is the most complex endpoint requiring:
        # 1. Time series analysis for monthly trends
        # 2. Growth rate calculations
        # 3. Customer value segmentation
        # 4. Product performance ranking
        # 5. Seasonal pattern detection
        # 6. Statistical analysis and forecasting
        
        # Placeholder return - replace with actual implementation
        return {
            "message": "Complex implementation needed",
            "requirements": [
                "Monthly revenue trends analysis",
                "Top performing products identification",
                "Revenue growth rate calculations",
                "Seasonal pattern analysis",
                "Category revenue distribution",
                "Customer value segmentation"
            ]
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating revenue insights: {str(e)}")

# Health check endpoint
@app.get("/health")
def health_check():
    """Simple health check endpoint"""
    return {
        "status": "healthy",
        "data_loaded": df is not None,
        "timestamp": datetime.now().isoformat()
    }

# Root endpoint with API information
@app.get("/")
def root():
    """API information and available endpoints"""
    return {
        "message": "E-commerce Analytics API",
        "version": "1.0.0",
        "endpoints": {
            "products": "/api/products - Product performance metrics",
            "dashboard": "/api/dashboard - Executive dashboard summary",
            "categories": "/api/categories - Category performance analysis",
            "demographics": "/api/demographics - Customer demographic insights",
            "revenue_insights": "/api/revenue-insights - Comprehensive revenue analysis"
        },
        "health": "/health - API health status"
    }

# Run the application
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)