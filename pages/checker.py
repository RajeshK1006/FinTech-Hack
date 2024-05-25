f_keywords = [
    "accounting", "assets", "balance sheet", "banking", "bonds", "budget", "capital", 
    "cash flow", "commodities", "credit", "cryptocurrency", "debt", "derivatives", 
    "dividends", "equities", "exchange rate", "financial planning", "fiscal policy", 
    "fixed income", "foreign exchange", "GDP", "gross domestic product", "hedge funds", 
    "inflation", "interest rates", "investment", "IPO", "initial public offering", 
    "liabilities", "liquidity", "loans", "market capitalization", "monetary policy", 
    "mutual funds", "options", "pension funds", "portfolio", "private equity", "real estate", 
    "REITs", "real estate investment trusts", "risk management", "savings", "securities", 
    "shares", "stock market", "taxation", "treasury", "venture capital", "wealth management", 
    "yield", "401(k)", "529 plan", "actuarial analysis", "annuities", "asset allocation", 
    "bear market", "bull market", "capital gains", "credit analysis", "diversification", 
    "dollar-cost averaging", "economic indicators", "financial ratios", "fundamental analysis", 
    "index funds", "leveraged buyout", "line of credit", "microfinance", "over-the-counter", 
    "penny stocks", "portfolio diversification", "price-to-earnings ratio", "profit margin", 
    "quantitative easing", "return on investment", "ROA", "ROE", "risk assessment", 
    "stock index", "stock options", "tax credits", "technical analysis", "underwriting", 
    "valuation", "variable interest rates", "venture funding", "volatility", "working capital", 
    "yield curve", "asset management", "balance of payments", "buy and hold", "capital budgeting", 
    "capital markets", "certificates of deposit", "CDs", "consumer price index", "CPI", 
    "discount rate", "discounted cash flow", "DCF", "earnings per share", "EPS", 
    "economic cycle", "enterprise value", "exchange-traded funds", "ETFs", "futures contracts", 
    "gross margin", "income statement", "individual retirement account", "IRA", "inflation rate", 
    "initial coin offering", "ICO", "institutional investor", "interest coverage ratio", 
    "investment banking", "junk bonds", "leverage ratio", "mutual fund", "net asset value", "NAV", 
    "net income", "net present value", "NPV", "price-earnings ratio", "private placement", 
    "profit and loss statement", "public offering", "retained earnings", "return on assets", 
    "ROA", "return on equity", "ROE", "return on investment", "ROI", "savings account", 
    "securitization", "shareholder equity", "short selling", "sovereign debt", "stock exchange", 
    "supply and demand", "swap contracts", "treasury bonds", "variable annuity", "venture capitalist", 
    "wealth management", "working capital management", "zero-coupon bond",

    # Added simpler terms
    "bank", "loan", "credit card", "mortgage", "payment", "savings account", "checking account", 
    "interest", "ATM", "debit card", "online banking", "mobile banking", "transfer", "deposit", 
    "withdrawal", "balance", "statement", "fees", "insurance", "premium", "policy", "claim", 
    "retirement", "pension", "salary", "wages", "income", "expense", "spending", "earnings", 
    "saving", "investing", "stocks", "bonds", "mutual funds", "ETFs", "dividends", "portfolio", 
    "financial advisor", "budgeting", "costs", "profits", "losses", "financial goals", 
    "emergency fund", "nest egg", "down payment", "credit score", "credit report", "debt management", 
    "financial security", "net worth", "assets", "liabilities", "monthly payment", "annual fee", 
    "late fee", "overdraft", "interest rate", "fixed rate", "variable rate", "principal", 
    "mortgage payment", "loan term", "equity", "appraisal", "refinancing", "escrow", "foreclosure",

    # Added payment app terms
    "balance", "transaction", "payment app", "digital wallet", "mobile wallet", "e-wallet", 
    "peer-to-peer payment", "P2P payment", "QR code payment", "payment request", "send money", 
    "receive money", "bill payment", "auto-pay", "recurring payment", "payment history", 
    "transaction history", "transaction fee", "service fee", "cashback", "rewards", "loyalty points", 
    "merchant", "vendor", "point of sale", "POS", "contactless payment", "NFC payment", 
    "secure payment", "authentication", "two-factor authentication", "2FA", "PIN", "biometric authentication", 
    "fraud detection", "fraud prevention", "encryption", "security code", "CVV", "account number", 
    "routing number", "invoice", "billing", "funds transfer", "ACH transfer", "direct deposit", 
    "mobile check deposit", "virtual card", "virtual account", "linked account", "funding source", 
    "payment gateway", "checkout", "subscription", "prepaid card", "gift card","save","savemoney","deposit","deposit money"
    # finance related jorgans
    "Account Balance", "Transaction History", "Payment Status", "Transaction Details", "Transaction Confirmation",
    "Payment Confirmation", "Payment Method", "Payment Options", "Payment Schedule", "Payment Reminder",
    "Bill Payment", "Bill Reminder", "Bill Due Date", "Invoice Payment", "Transfer Confirmation", "Transfer Status",
    "Transfer Details", "Transfer Limits", "Transfer Confirmation Number", "Transfer Receipt", "Transfer Tracking",
    "Transfer Time", "Transfer Method", "Transfer Notification", "Transfer Authorization", "Transfer Error",
    "Account Verification", "Account Security", "Account Settings", "Account Information", "Account Management",
    "Account Verification Process", "Account Verification Status", "Account Verification Time", "Account Verification Method",
    "Account Verification Code", "Account Verification Error", "Account Verification Confirmation", "Account Verification Failure",
    "Transaction Authorization", "Transaction Verification", "Transaction Confirmation Code", "Transaction Confirmation Number",
    "Transaction Error", "Transaction Declined", "Transaction Approval", "Transaction Authorization Code", "Transaction Authorization Error",
    "Transaction Pending", "Transaction Processing", "Transaction Failed", "Transaction Approved", "Transaction Verification Process",
    "Transaction Verification Status", "Transaction Verification Time", "Transaction Verification Method", "Transaction Verification Code",
    "Transaction Verification Error", "Transaction Verification Confirmation", "Transaction Verification Failure", "Transaction History",
    "Transaction Summary", "Transaction Report", "Transaction Log", "Transaction Tracking", "Transaction Record",
    "Transaction Summary", "Transaction Details", "Transaction Information", "Transaction Status", "Transaction Processing Time",
    "Transaction Amount", "Transaction Currency", "Transaction Fee", "Transaction Completion", "Transaction Confirmation",
    "Transaction Confirmation Number", "Transaction Confirmation Code", "Transaction Confirmation Error", "Transaction Confirmation Status",
    "Transaction Confirmation Message", "Transaction Confirmation Receipt", "Transaction Confirmation Email", "Transaction Confirmation SMS",
    "Transaction Confirmation Alert", "Transaction Confirmation Notification", "Transaction Confirmation Failure", "Transaction Confirmation Success",
    "Transaction Confirmation Time", "Transaction Confirmation Method", "Transaction Confirmation Process", "Transaction Confirmation Authorization",
    "Transaction Confirmation Verification", "Transaction Confirmation Declined", "Transaction Confirmation Approved", "Transaction Confirmation Pending",
    "Transaction Confirmation Processing", "Transaction Confirmation Completed", "Transaction Confirmation Log", "Transaction Confirmation Report",
    "Transaction Confirmation Summary", "Transaction Confirmation Details", "Transaction Confirmation Record", "Transaction Confirmation Tracking",
    "Transaction Confirmation Information", "Transaction Confirmation Amount", "Transaction Confirmation Currency", "Transaction Confirmation Fee",
    "Transaction Confirmation Completion", "Transaction Confirmation Verification", "Transaction Confirmation Authorization", "Transaction Confirmation Verification Process",
    "Transaction Confirmation Verification Status", "Transaction Confirmation Verification Time", "Transaction Confirmation Verification Method", "Transaction Confirmation Verification Code",
    "Transaction Confirmation Verification Error", "Transaction Confirmation Verification Confirmation", "Transaction Confirmation Verification Failure", "Transaction Confirmation Verification Success",
    "Transaction Confirmation Verification Declined", "Transaction Confirmation Verification Approved", "Transaction Confirmation Verification Pending", "Transaction Confirmation Verification Processing",
    "Transaction Confirmation Verification Completed", "Transaction Confirmation Verification Log", "Transaction Confirmation Verification Report", "Transaction Confirmation Verification Summary",
    "Transaction Confirmation Verification Details", "Transaction Confirmation Verification Record", "Transaction Confirmation Verification Tracking", "Transaction Confirmation Verification Information",
    "Transaction Confirmation Verification Amount", "Transaction Confirmation Verification Currency", "Transaction Confirmation Verification Fee", "Transaction Confirmation Verification Completion",
    "Transaction Confirmation Authorization", "Transaction Confirmation Verification Authorization", "Transaction Confirmation Authentication", "Transaction Confirmation Verification Authentication",
    "Transaction Confirmation Authorization Process", "Transaction Confirmation Verification Authorization Process", "Transaction Confirmation Authentication Process", "Transaction Confirmation Verification Authentication Process",
    "Transaction Confirmation Authorization Status", "Transaction Confirmation Verification Authorization Status", "Transaction Confirmation Authentication Status", "Transaction Confirmation Verification Authentication Status",
    "Transaction Confirmation Authorization Time", "Transaction Confirmation Verification Authorization Time", "Transaction Confirmation Authentication Time", "Transaction Confirmation Verification Authentication Time",
    "Transaction Confirmation Authorization Method", "Transaction Confirmation Verification Authorization Method", "Transaction Confirmation Authentication Method", "Transaction Confirmation Verification Authentication Method",
    "Transaction Confirmation Authorization Code", "Transaction Confirmation Verification Authorization Code", "Transaction Confirmation Authentication Code", "Transaction Confirmation Verification Authentication Code",
    "Transaction Confirmation Authorization Error", "Transaction Confirmation Verification Authorization Error", "Transaction Confirmation Authentication Error", "Transaction Confirmation Verification Authentication Error",
    "Transaction Confirmation Authorization Confirmation", "Transaction Confirmation Verification Authorization Confirmation", "Transaction Confirmation Authentication Confirmation", "Transaction Confirmation Verification Authentication Confirmation",
    "Transaction Confirmation Authorization Failure", "Transaction Confirmation Verification Authorization Failure", "Transaction Confirmation Authentication Failure", "Transaction Confirmation Verification Authentication Failure",
    "Transaction Confirmation Authorization Success", "Transaction Confirmation Verification Authorization Success", "Transaction Confirmation Authentication Success", "Transaction Confirmation Verification Authentication Success",
    "Transaction Confirmation Authorization Pending", "Transaction Confirmation Verification Authorization Pending", "Transaction Confirmation Authentication Pending", "Transaction Confirmation Verification Authentication Pending",
    "Transaction Confirmation Authorization Processing", "Transaction Confirmation Verification Authorization Processing", "Transaction Confirmation Authentication Processing", "Transaction Confirmation Verification Authentication Processing",
    "Transaction Confirmation Authorization Completed", "Transaction Confirmation Verification Authorization Completed", "Transaction Confirmation Authentication Completed", "Transaction Confirmation Verification Authentication Completed",
    "Transaction Confirmation Authorization Log", "Transaction Confirmation Verification Authorization Log", "Transaction Confirmation Authentication Log", "Transaction Confirmation Verification Authentication Log",
    "Transaction Confirmation Authorization Report", "Transaction Confirmation Verification Authorization Report", "Transaction Confirmation Authentication Report", "Transaction Confirmation Verification Authentication Report",
    "Transaction Confirmation Authorization Summary", "Transaction Confirmation Verification Authorization Summary", "Transaction Confirmation Authentication Summary", "Transaction Confirmation Verification Authentication Summary",
    "Transaction Confirmation Authorization Details", "Transaction Confirmation Verification Authorization Details", "Transaction Confirmation Authentication Details", "Transaction Confirmation Verification Authentication Details",
    "Transaction Confirmation Authorization Record", "Transaction Confirmation Verification Authorization Record", "Transaction Confirmation Authentication Record", "Transaction Confirmation Verification Authentication Record",
    "Transaction Confirmation Authorization Tracking", "Transaction Confirmation Verification Authorization Tracking", "Transaction Confirmation Authentication Tracking", "Transaction Confirmation Verification Authentication Tracking",
    "Transaction Confirmation Authorization Information", "Transaction Confirmation Verification Authorization Information", "Transaction Confirmation Authentication Information", "Transaction Confirmation Verification Authentication Information",
    "Transaction Confirmation Authorization Amount", "Transaction Confirmation Verification Authorization Amount", "Transaction Confirmation Authentication Amount", "Transaction Confirmation Verification Authentication Amount",
    "Transaction Confirmation Authorization Currency", "Transaction Confirmation Verification Authorization Currency", "Transaction Confirmation Authentication Currency", "Transaction Confirmation Verification Authentication Currency",
    "Transaction Confirmation Authorization Fee", "Transaction Confirmation Verification Authorization Fee", "Transaction Confirmation Authentication Fee", "Transaction Confirmation Verification Authentication Fee",
    "Transaction Confirmation Authorization Completion", "Transaction Confirmation Verification Authorization Completion", "Transaction Confirmation Authentication Completion", "Transaction Confirmation Verification Authentication Completion",
    "Transaction Confirmation Verification", "Transaction Confirmation Verification Status", "Transaction Confirmation Verification Time", "Transaction Confirmation Verification Method",
    "Transaction Confirmation Verification Code", "Transaction Confirmation Verification Error", "Transaction Confirmation Verification Confirmation", "Transaction Confirmation Verification Failure",
    "Transaction Confirmation Verification Success", "Transaction Confirmation Verification Declined", "Transaction Confirmation Verification Approved", "Transaction Confirmation Verification Pending",
    "Transaction Confirmation Verification Processing", "Transaction Confirmation Verification Completed", "Transaction Confirmation Verification Log",
    
    # savings
    
    
    # Banking
    "Bank", "Account", "Deposit", "Withdrawal", "Checking", "Savings", "ATM", "Branch", "Teller",
    "Transaction", "Transfer", "Online Banking", "Mobile Banking", "Debit Card", "Credit Card",
    "Loan", "Mortgage", "Interest", "Investment", "Interest Rate", "Currency Exchange", "Foreign Currency",
    "Overdraft", "Bank Statement", "Banking Fee", "Bank Account Balance", "Bank Account Number",
    "Bank Account Statement", "Bank Account Holder", "Banking Hours", "Banking Services", "Banking Institution",
    "Banking Regulation", "Banking Security", "Banking Sector", "Banking Facility", "Banking System",
    
    # Savings
    "Savings Account", "Interest Rate", "Compound Interest", "Saving Plan", "Emergency Fund",
    "Retirement Savings", "Savings Goal", "Automatic Savings", "High-Yield Savings", "Saving Strategy",
    "Savings Withdrawal", "Savings Balance", "Savings Contribution", "Savings Account Statement",
    "Saving Habit", "Saving Target", "Saving Interest", "Saving Account Fees", "Saving Account Options",
    "Saving Account Benefits", "Savings Account Holder", "Savings Account Number", "Savings Account Interest",
    "Savings Account Balance", "Savings Account Management", "Savings Account Limit", "Savings Account Transfer",
    "Savings Account Withdrawal", "Savings Account Security", "Savings Account Terms", "Savings Account Types",
    
    # Budgeting
    "Budget", "Expense", "Income", "Budgeting Tool", "Budget Planner", "Budget Tracker", "Budgeting App",
    "Monthly Budget", "Annual Budget", "Budget Allocation", "Budget Management", "Budgeting Worksheet",
    "Budget Review", "Budget Adjustment", "Budgeting Strategy", "Budget Limit", "Budget Category",
    "Budget Forecast", "Budget Analysis", "Budgeting Software", "Budgeting Goals", "Budgeting Process",
    "Budgeting Techniques", "Budgeting Methods", "Budgeting Principles", "Budgeting Model", "Budgeting Cycle",
    "Budgeting Framework", "Budgeting Tool", "Budgeting Exercise", "Budgeting Tips", "Budgeting Rules",
    "Budgeting Discipline", "Budgeting Accountability", "Budgeting Awareness", "Budgeting Knowledge",
    "Budgeting Behavior", "Budgeting Control", "Budgeting Evaluation", "Budgeting Plan", "Budgeting Review",
    "Budgeting Discipline", "Budgeting Responsibility", "Budgeting Efficiency", "Budgeting Monitoring",
    "Budgeting Feedback", "Budgeting Improvement", "Budgeting Success", "Budgeting Progress",
    "Budgeting Performance", "Budgeting Optimization", "Budgeting Enhancement", "Budgeting Effectiveness"


]


def checking(query):
    flag = False
    list_of_words = query.split(" ")
    for i in list_of_words:
        if i.lower() in f_keywords:
            flag = True
            break
    return flag