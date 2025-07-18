# 🏆 E-commerce Analytics API - Hackathon Challenge

Welcome to the **E-commerce Analytics API Hackathon**! Test your data science and debugging skills by completing three challenging endpoints.

## 🎯 Challenge Overview

Your mission is to fix and complete three API endpoints:
1. **`POST /api/get-top-month`** - Modify to return TOP 5 products (Easy)
2. **`GET /api/categories`** - Complete the implementation (Medium) 
3. **`GET /api/demographics`** - Debug multiple bugs (Hard)

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

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/alumnx-ai-labs/codeathon.git
cd codeathon
```

### 2. Create Virtual Environment

#### For Linux/Mac:
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate
```

#### For Windows:
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# For Command Prompt:
venv\Scripts\activate

# For PowerShell:
venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the FastAPI Service

```bash
# Start the development server
uvicorn solution_script:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at:
- **Main URL**: http://localhost:8000
- **Health Check**: http://localhost:8000/health

## 🧪 Testing the API

### Health Check
```bash
curl http://localhost:8000/health
```

### Data Info (Debug Helper)
```bash
curl http://localhost:8000/api/data-info
```

## 📋 Challenge Details & API Endpoints

### 🎯 Challenge 1: `/api/get-top-month` (Easy - 20 points)

**Task**: Modify to return TOP 5 products instead of TOP 3

#### Request:
```bash
curl -X POST "http://localhost:8000/api/get-top-month" \
     -H "Content-Type: application/json" \
     -d '{"month": "2024-03"}'
```

#### Expected Response:
```json
{
  "month": "2024-03",
  "top_products": [
    {
      "product_name": "Laptop Pro",
      "revenue": 1500.00,
      "category": "Electronics"
    },
    {
      "product_name": "Smartphone X",
      "revenue": 1200.00,
      "category": "Electronics"
    }
    // ... 3 more products (total 5)
  ],
  "total_revenue": 15000.00
}
```

**What to do**: Find and change the line that limits results to 3 products.

---

### 🎯 Challenge 2: `/api/categories` (Medium - 40 points)

**Task**: Complete the entire implementation from scratch

#### Request:
```bash
curl http://localhost:8000/api/categories
```

#### Expected Response:
```json
{
  "categories": [
    {
      "category": "Electronics",
      "total_revenue": 15000.50,
      "avg_revenue_per_transaction": 125.25,
      "transaction_count": 120,
      "avg_rating": 4.2,
      "total_units_sold": 350,
      "revenue_percentage": 35.5
    }
    // ... more categories
  ],
  "total_categories": 6
}
```

**What to do**: 
- Implement groupby operations on sales data
- Calculate all required metrics
- Handle null values appropriately
- Calculate revenue percentages

---

### 🎯 Challenge 3: `/api/demographics` (Hard - 40 points)

**Task**: Debug and fix multiple bugs in the code

#### Request:
```bash
curl http://localhost:8000/api/demographics
```

#### Expected Response:
```json
{
  "age_groups": [
    {
      "age_range": "18-25",
      "customer_count": 150,
      "avg_spending": 85.50,
      "total_revenue": 12825.00,
      "avg_rating": 4.1,
      "transaction_count": 150,
      "revenue_percentage": 25.5
    }
    // ... more age groups
  ],
  "summary": {
    "total_customers": 600,
    "highest_spending_group": "26-35",
    "largest_group": "26-35", 
    "highest_rated_group": "46-55"
  }
}
```

**What to do**:
- Fix syntax errors that cause crashes
- Debug column mapping issues
- Fix variable naming problems
- Correct calculation logic
- Handle missing data appropriately

**Hints for debugging**:
- Check error messages carefully
- Verify column names match the dataset
- Ensure aggregation columns align with assignments
- Test each section independently

## 🚀 Deployment to Render

### Option 1: Manual Deployment (Recommended for beginners)

1. **Create Render Account**: Sign up at [render.com](https://render.com)
2. **Connect GitHub**: Link your GitHub account to Render
3. **Create Web Service**: 
   - Click "New" → "Web Service"
   - Connect your repository
   - Configure the service:
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `uvicorn solution_script:app --host 0.0.0.0 --port $PORT`
     - **Python Version**: 3.9+
4. **Deploy**: Click "Create Web Service"

### Option 2: Using render.yaml (Advanced)

If you want to use Infrastructure as Code, create a `render.yaml` file:

```yaml
services:
  - type: web
    name: ecommerce-analytics-api
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: uvicorn solution_script:app --host 0.0.0.0 --port $PORT
    envVars:
      - key: PYTHON_VERSION
        value: 3.9.16
```

**Benefits of render.yaml**:
- ✅ Automatic configuration deployment
- ✅ Version control for infrastructure settings
- ✅ Consistent deployments across environments
- ✅ Easy to replicate and share configurations

**When to use render.yaml**:
- You want infrastructure as code
- You need consistent deployment settings
- You're deploying multiple services
- You want to version control your deployment configuration

### 3. Environment Variables

No additional environment variables needed for this challenge.

## 📚 Documentation References

### FastAPI Resources
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/)
- [Pydantic Models](https://pydantic-docs.helpmanual.io/)

### Pandas Resources  
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [GroupBy Operations](https://pandas.pydata.org/docs/user_guide/groupby.html)
- [Data Aggregation](https://pandas.pydata.org/docs/user_guide/groupby.html#aggregation)

### Python Debugging
- [Python Debugging Guide](https://realpython.com/python-debugging-pdb/)
- [Common Python Errors](https://realpython.com/python-traceback/)

### Deployment
- [Render Deployment Guide](https://render.com/docs)
- [Python Apps on Render](https://render.com/docs/deploy-fastapi)

## 🏆 Scoring Criteria

- **Challenge 1**: 20 points - Simple modification
- **Challenge 2**: 40 points - Complete implementation  
- **Challenge 3**: 40 points - Multiple bug fixes
- **Bonus Points**: Code quality, error handling, documentation

## 🛠️ Development Tips

1. **Use the `/api/data-info` endpoint** to understand the dataset structure
2. **Test incrementally** - fix one bug at a time
3. **Read error messages carefully** - they contain valuable debugging info
4. **Use curl commands or Postman** for API testing
5. **Check column names** in the actual CSV file if needed

## 🆘 Getting Help

- Check the API endpoints using curl commands or Postman
- Use the `/health` endpoint to verify the service is running
- Use the `/api/data-info` endpoint to inspect the dataset
- Review error logs in the terminal for debugging clues

## 📝 Submission

1. Complete all three challenges
2. Test all endpoints locally
3. Deploy to Render 
4. **Submit your Render deployment URL** (e.g., `https://your-app-name.onrender.com`)

**Note**: Make sure your deployed API is working and all endpoints are accessible before submission.

Good luck, and may the best data scientist win! 🚀

---

**Happy Coding!** 🎉