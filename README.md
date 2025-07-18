# E-commerce Analytics API - Code-a-thon Challenge

A FastAPI-based analytics dashboard for e-commerce transaction data analysis. This API provides insights into sales performance, customer demographics, and product analytics for business intelligence.

## 🚀 Quick Setup

### 1. Clone and Setup
```bash
# Clone the repository
git clone https://github.com/alumnx-ai-labs/code-a-thon.git
cd code-a-thon

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Run Locally
```bash
# Start the FastAPI server
python main.py

# Or using uvicorn directly
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### 3. Test the API
```bash
# Check API health
curl http://localhost:8000/health

# Test an endpoint
curl http://localhost:8000/api/products
```

**Expected Response:**
```json
{
  "products": [
    {
      "product_name": "Gaming Laptop"
    }
  ],
  "total_products": 20,
  "summary": {
    "total_revenue": 15234.50
  }
}
```

## 📊 API Endpoints Guide

> 📋 **For detailed request/response payloads and implementation requirements, see [APICONFIG.md](APICONFIG.md)**

### Enhancement Challenge - Basic
**`GET /api/products`** - Product Performance Metrics
- **Business Purpose**: Inventory management and product performance analysis
- **Current Status**: ✅ Working but incomplete - missing key business metrics
- **Enhancement Required**: Add `price`, `total_count`, `average_rating`, `total_revenue`, and `category` fields for each product
- **Your Task**: Transform basic product list into comprehensive product performance analytics
- **Usage**: Provides product managers with KPIs for inventory and pricing decisions
- **Sample Request**: `curl http://localhost:8000/api/products`

### Debug Challenge - Intermediate  
**`GET /api/categories`** - Category Performance Analysis
- **Business Purpose**: Merchandising team insights for inventory optimization and category management
- **Current Status**: 🐛 Broken with multiple complex data science bugs
- **Your Task**: Debug 5 subtle data processing errors affecting revenue calculations and metrics
- **Known Issues**: 
  - Incorrect aggregation methods
  - Wrong column references for calculations
  - Missing error handling for edge cases
  - Improper data type handling
- **Sample Request**: `curl http://localhost:8000/api/categories`

### Build-from-Scratch - Advanced
**`GET /api/revenue-insights`** - Comprehensive Revenue Analysis
- **Business Purpose**: CFO and strategic planning for budget forecasting and growth strategy
- **Current Status**: 🔧 Empty function with placeholder data - needs complete implementation
- **Your Task**: Build comprehensive revenue analytics with advanced business intelligence
- **Requirements**:
  - **Monthly Trends**: Revenue analysis with month-over-month growth rates
  - **Top Products**: Revenue ranking and contribution analysis (top 2 products only)
  - **Category Distribution**: Revenue breakdown by product category
  - **Customer Segmentation**: High/Medium/Low value customer analysis based on spending
  - **Growth Metrics**: Overall growth rates, trend identification, seasonal patterns
  - **Forecasting**: Predictive analytics for next month revenue with confidence levels
- **Sample Request**: `curl http://localhost:8000/api/revenue-insights`

## 🎯 Challenge Objectives

### Enhancement Task (20 points)
**Improve the `/api/products` endpoint by adding missing business metrics:**
- `price` field for each product (current product price)
- `total_count` field for each product (total units sold)
- `average_rating` field for each product (average customer rating)
- `total_revenue` field for each product (total revenue generated)
- `category` field for each product (product category)
- Enhanced summary section with additional statistics (top performer, lowest performer, average rating)

### Debug Task (30 points)
**Fix all bugs in `/api/categories` endpoint:**
1. Identify and fix incorrect aggregation methods
2. Correct wrong column references in calculations  
3. Add proper error handling for division by zero
4. Fix data type and NaN value handling issues
5. Correct count calculations using appropriate data

### Implementation Task (50 points)
**Complete `/api/revenue-insights` endpoint with advanced analytics:**
- Monthly revenue trends with growth rate calculations
- Top 2 products by revenue with contribution percentages
- Category revenue distribution analysis
- Customer value segmentation (High: >$200, Medium: $50-$200, Low: <$50)
- Growth metrics and trend analysis
- Revenue forecasting with business insights

## 📋 Dataset Information

The `sales_data.csv` contains 250 e-commerce transactions with:
- **Products**: 20+ unique items across 6 categories
- **Categories**: Electronics, Clothing, Books, Home, Sports, Beauty
- **Time Range**: 6 months of sales data (Jan-Aug 2024)
- **Customers**: Ages 18-65 for demographic analysis
- **Test Data**: "Test Widget" entries for auto-evaluation

### Key Columns
- `transaction_id`: Unique transaction identifier
- `product_name`: Product names (includes "Test Widget" for testing)
- `category`: Product categories for analysis
- `price`: Product prices ($5-$2000 range)
- `quantity`: Purchase quantities (1-5 items)
- `customer_age`: Customer ages (18-65)
- `purchase_date`: Transaction dates
- `customer_rating`: Product ratings (1-5 stars, some missing)
- `revenue`: Calculated revenue (price × quantity)

## 🚀 Deployment

### Deploy to Render

1. **Prepare Repository**
   ```bash
   # Make sure virtual environment is activated
   source venv/bin/activate  # On macOS/Linux
   # or
   venv\Scripts\activate     # On Windows
   
   # Test your API locally first
   python main.py
   
   # Commit your changes
   git add .
   git commit -m "Complete e-commerce analytics API"
   git push origin main
   ```

2. **Render Setup**
   - Go to [Render.com](https://render.com)
   - Connect your GitHub repository
   - Create new "Web Service"

3. **Configuration**
   ```
   Build Command: pip install -r requirements.txt
   Start Command: python main.py
   Environment: Python 3
   Port: 8000
   ```

4. **Environment Variables**
   ```
   PYTHON_VERSION=3.9
   ```

### Alternative: Deploy to Railway/Heroku
```bash
# For Railway
railway login
railway init
railway up

# For Heroku
heroku create your-api-name
git push heroku main
```

## 📝 Submission Format

### Required Files
```
code-a-thon/
├── main.py           # ✅ Complete FastAPI application
├── requirements.txt  # ✅ Python dependencies
├── sales_data.csv    # ✅ E-commerce transaction dataset
├── APICONFIG.md      # ✅ Detailed API request/response documentation
└── README.md         # ✅ This setup guide
```

### Submission Checklist
- [ ] **Enhancement** (20 pts): `/api/products` endpoint improved with price, total_count, average_rating, total_revenue, and category fields
- [ ] **Debug Challenge** (30 pts): `/api/categories` all 5 bugs identified and fixed
- [ ] **Advanced Implementation** (50 pts): `/api/revenue-insights` fully implemented with comprehensive analytics
- [ ] **Code Quality**: Clean, documented code with proper error handling
- [ ] **Testing**: All endpoints tested and returning expected responses
- [ ] **Deployment**: API successfully deployed and accessible

## 🔧 Development Tips

### Data Analysis Hints for Revenue Insights
```python
# Monthly trends analysis
df['month'] = df['purchase_date'].dt.to_period('M')
monthly_data = df.groupby('month')['revenue'].sum()

# Growth rate calculation
prev_revenue = None
for month, revenue in monthly_data.items():
    if prev_revenue is not None:
        growth_rate = ((revenue - prev_revenue) / prev_revenue) * 100
    prev_revenue = revenue

# Customer value segmentation
def categorize_customer_value(revenue):
    if revenue > 200:
        return "High Value"
    elif revenue >= 50:
        return "Medium Value"
    else:
        return "Low Value"

# Top products analysis
top_products = df.groupby('product_name')['revenue'].sum().nlargest(2)
```

### Common Debug Issues in Categories Endpoint
1. **Aggregation Methods**: Check if using correct aggregation functions (mean vs first)
2. **Column References**: Verify using correct column names for calculations
3. **Division by Zero**: Add proper checks before percentage calculations
4. **Data Types**: Handle NaN values and data type conversions properly
5. **Count Logic**: Ensure using appropriate columns for counting categories vs products

### Products Enhancement Guidelines
```python
# Product-level aggregations needed
product_metrics = sales_df.groupby('product_name').agg({
    'price': 'first',           # Current price
    'quantity': 'sum',          # Total units sold
    'customer_rating': 'mean',  # Average rating
    'revenue': 'sum',          # Total revenue
    'category': 'first'        # Product category
})

# Summary statistics for enhanced response
total_revenue = sales_df['revenue'].sum()
avg_rating = sales_df['customer_rating'].mean()
top_performer = product_metrics['revenue'].idxmax()
lowest_performer = product_metrics['revenue'].idxmin()
```

### API Best Practices
- Always include try-catch blocks for error handling
- Round monetary values to 2 decimal places
- Handle missing/NaN values appropriately
- Use consistent response formats across endpoints
- Include business context in docstrings
- Validate data before calculations

### Expected Response Formats
For detailed API specifications including request/response payloads, field requirements, and expected data formats, refer to **[APICONFIG.md](APICONFIG.md)**.

## 📚 Resources

### FastAPI Documentation
- [FastAPI Official Docs](https://fastapi.tiangolo.com/)
- [Query Parameters](https://fastapi.tiangolo.com/tutorial/query-params/)
- [Response Models](https://fastapi.tiangolo.com/tutorial/response-model/)

### Pandas for Data Analysis
- [GroupBy Operations](https://pandas.pydata.org/docs/user_guide/groupby.html)
- [Time Series Analysis](https://pandas.pydata.org/docs/user_guide/timeseries.html)
- [Data Aggregation](https://pandas.pydata.org/docs/user_guide/aggregation.html)

### Deployment Platforms
- [Render Deployment Guide](https://render.com/docs/deploy-fastapi)
- [Railway Documentation](https://docs.railway.app/)
- [Heroku Python Guide](https://devcenter.heroku.com/articles/getting-started-with-python)

## 🆘 Troubleshooting

### Common Issues

**API won't start:**
```bash
# Make sure virtual environment is activated
source venv/bin/activate  # On macOS/Linux
# or
venv\Scripts\activate     # On Windows

# Check if all dependencies are installed
pip install -r requirements.txt

# Verify Python version (3.8+)
python --version

# Check for syntax errors
python -m py_compile main.py
```

**Data loading errors:**
```bash
# Ensure sales_data.csv is in the same directory as main.py
ls -la sales_data.csv

# Check CSV format
head -5 sales_data.csv
```

**Import errors:**
```bash
# Make sure virtual environment is activated first
source venv/bin/activate  # On macOS/Linux
# or  
venv\Scripts\activate     # On Windows

# Install missing packages
pip install fastapi uvicorn pandas numpy python-dateutil

# Clear Python cache
rm -rf __pycache__
```

**Virtual Environment Issues:**
```bash
# If virtual environment is not working, recreate it
rm -rf venv
python -m venv venv
source venv/bin/activate  # On macOS/Linux
# or
venv\Scripts\activate     # On Windows
pip install -r requirements.txt
```

### Testing Endpoints
```bash
# Test all available endpoints
curl http://localhost:8000/health
curl http://localhost:8000/api/products
curl http://localhost:8000/api/categories
curl http://localhost:8000/api/revenue-insights
```

### Performance Optimization
- Use appropriate pandas data types (category, int16, float32)
- Implement caching for expensive calculations
- Optimize groupby operations
- Handle large datasets efficiently

## 🎉 Success Indicators

### Working API Signs
- ✅ All endpoints return 200 status codes
- ✅ JSON responses match expected format
- ✅ No 500 internal server errors
- ✅ Products endpoint shows enhanced metrics
- ✅ Categories endpoint provides accurate analytics
- ✅ Revenue insights include comprehensive forecasting data

### Bonus Points
- 🌟 Additional business insights beyond requirements
- 🌟 Advanced analytics (trend analysis, seasonality detection)
- 🌟 Comprehensive error handling with meaningful messages
- 🌟 Performance optimizations for large datasets
- 🌟 Creative business intelligence features

Good luck with your e-commerce analytics API challenge! 🚀