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
      "product_name": "Gaming Laptop",
      "price": 1299.99,
      "total_count": 2
    }
  ],
  "total_products": 20
}
```

## 📊 API Endpoints Guide

### Working Enhancement Endpoint
**`GET /api/products`** - Product Performance Metrics
- **Business Purpose**: Inventory management and product performance analysis
- **Current Status**: ✅ Working but incomplete
- **Enhancement Required**: Add `average_rating`, `total_revenue`, `category`, and summary section
- **Usage**: Provides product managers with KPIs for decision making

### Easy Debug Challenge
**`GET /api/dashboard?days=30`** - Executive Dashboard Summary
- **Business Purpose**: C-suite KPIs for strategic decisions
- **Current Status**: 🐛 Broken with obvious bugs
- **Your Task**: Fix date filtering, aggregation methods, and calculation errors
- **Sample Request**: `curl http://localhost:8000/api/dashboard?days=30`

### Intermediate Debug Challenge
**`GET /api/categories`** - Category Performance Analysis
- **Business Purpose**: Merchandising team insights for inventory optimization
- **Current Status**: 🐛 Broken with complex logic errors
- **Your Task**: Fix groupby operations, percentage calculations, and data processing
- **Sample Request**: `curl http://localhost:8000/api/categories`

### Build-from-Scratch - Intermediate
**`GET /api/demographics`** - Customer Demographics Analysis
- **Business Purpose**: Marketing team segmentation for targeted campaigns
- **Current Status**: 🔧 Empty function - needs complete implementation
- **Requirements**:
  - Age group analysis (18-25, 26-35, 36-45, 46-55, 56+)
  - Spending patterns by demographic
  - Average ratings by age group
  - Transaction frequency analysis
- **Sample Request**: `curl http://localhost:8000/api/demographics`

### Build-from-Scratch - Advanced
**`GET /api/revenue-insights`** - Comprehensive Revenue Analysis
- **Business Purpose**: CFO and strategic planning for budget and growth strategy
- **Current Status**: 🔧 Empty function - complex analytical implementation needed
- **Requirements**:
  - Monthly revenue trends with growth rates
  - Top performing products by revenue
  - Customer value segmentation (high/medium/low)
  - Seasonal pattern identification
  - Revenue forecasting insights
- **Sample Request**: `curl http://localhost:8000/api/revenue-insights`

## 🎯 Challenge Objectives

### Enhancement Task
Improve the working `/api/products` endpoint by adding:
- `average_rating` field for each product
- `total_revenue` field for each product  
- `category` field for each product
- Summary section with overall statistics

### Debug Tasks
1. **Easy**: Fix obvious bugs in `/api/dashboard` (date logic, aggregations)
2. **Intermediate**: Resolve complex issues in `/api/categories` (groupby, calculations)

### Implementation Tasks
1. **Intermediate**: Complete `/api/demographics` with age group analysis
2. **Advanced**: Build comprehensive `/api/revenue-insights` with forecasting

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
├── APICONFIG.md      # ✅ API request/response documentation
└── README.md         # ✅ This setup guide
```

### Submission Checklist
- [ ] **Easy Debug** (10 pts): `/api/dashboard` bugs fixed and working correctly
- [ ] **Intermediate Debug** (20 pts): `/api/categories` complex issues resolved
- [ ] **Enhancement** (20 pts): `/api/products` endpoint improved with additional fields
- [ ] **Intermediate Build** (25 pts): `/api/demographics` fully implemented
- [ ] **Advanced Build** (25 pts): `/api/revenue-insights` complete with forecasting
- [ ] **Code Quality**: Clean, documented code with proper error handling
- [ ] **Testing**: All endpoints tested and returning expected responses

## 🔧 Development Tips

### Data Analysis Hints
```python
# Age group segmentation
age_bins = [17, 25, 35, 45, 55, 100]
age_labels = ['18-25', '26-35', '36-45', '46-55', '56+']
df['age_group'] = pd.cut(df['customer_age'], bins=age_bins, labels=age_labels)

# Monthly trends
df['month'] = df['purchase_date'].dt.to_period('M')
monthly_data = df.groupby('month')['revenue'].sum()

# Customer segmentation by spending
def categorize_customer_value(avg_order):
    if avg_order > 200:
        return "High Value"
    elif avg_order > 50:
        return "Medium Value"
    else:
        return "Low Value"
```

### Common Debug Issues
1. **Date Filtering**: Use `datetime.now() - timedelta(days=days)` not plus
2. **Aggregation**: Use correct column names (`revenue` not `price` for totals)
3. **Percentage Calculation**: Multiply by 100, not 10
4. **GroupBy**: Remember to call `reset_index()` when needed
5. **Missing Values**: Handle NaN ratings with `dropna()` or fillna methods

### API Best Practices
- Always include try-catch blocks for error handling
- Validate query parameters with FastAPI's Query validators
- Return consistent response formats across endpoints
- Include business context in docstrings
- Round monetary values to 2 decimal places

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
# Test all endpoints
curl http://localhost:8000/
curl http://localhost:8000/health
curl http://localhost:8000/api/products
curl http://localhost:8000/api/dashboard?days=30
curl http://localhost:8000/api/categories
curl http://localhost:8000/api/demographics
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
- ✅ JSON responses match expected format in APICONFIG.md
- ✅ No 500 internal server errors
- ✅ Dashboard shows realistic business metrics
- ✅ Demographics endpoint provides age group insights
- ✅ Revenue insights include forecasting data

### Bonus Points
- 🌟 Additional business insights beyond requirements
- 🌟 Creative data visualizations in responses
- 🌟 Advanced analytics (forecasting, trend analysis)
- 🌟 Comprehensive error handling with meaningful messages
- 🌟 Performance optimizations for large datasets

Good luck with your e-commerce analytics API! 🚀