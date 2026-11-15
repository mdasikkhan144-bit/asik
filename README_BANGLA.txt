ASIK PERSONAL PORTFOLIO — FRONTEND + BACKEND

যা যা আছে:
- Frontend: HTML, CSS, JavaScript
- Backend: Python Flask
- Database: SQLite (portfolio.db স্বয়ংক্রিয়ভাবে তৈরি হবে)
- Contact form: তথ্য backend-এ সেভ হবে
- Local message inbox: /admin/messages

চালানোর নিয়ম (Windows 11):
1. ZIP ফাইল Extract করো।
2. Extract করা ফোল্ডার VS Code-এ Open করো।
3. VS Code Terminal খুলে লিখো:
   py -m venv .venv
4. Virtual environment চালু করো:
   .venv\Scripts\activate
5. Flask install করো:
   pip install -r requirements.txt
6. Website চালাও:
   py app.py
7. Browser-এ খোলো:
   http://127.0.0.1:5000

Contact form পরীক্ষা:
- ওয়েবসাইটে Contact অংশে নাম, ইমেইল, মেসেজ দিয়ে Send message চাপো।
- Saved messages দেখতে ব্রাউজারে যাও:
  http://127.0.0.1:5000/admin/messages

গুরুত্বপূর্ণ:
- এটি শেখার জন্য local demo project।
- /admin/messages পেজে এখন login protection নেই। ইন্টারনেটে deploy করার আগে
  অবশ্যই authentication, CSRF protection, production secret key এবং নিরাপত্তা
  ব্যবস্থা যোগ করতে হবে।
- app.py-তে debug=True শুধু local development-এর জন্য।
- নিজের নাম, পরিচিতি, skills ও projects templates/index.html ফাইলে বদলাতে পারো।
