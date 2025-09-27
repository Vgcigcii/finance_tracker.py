# import streamlit as st
import json
import pandas as pd
# from datetime import date
import matplotlib.pyplot as plt
# file_path = "User_Expense_Data"
# st.title("💰 Expense Tracker")
# #Header and text
# menu = ["Add Expense","View Expenses","Summary"]
# st.header("Welcome to the app")
# user_choice = st.sidebar.selectbox("Menu",menu)
# if user_choice=="Add Expense":
#     st.subheader("Enter the amount you spend here")
#     Category  = st.text_input(label="Please enter the type of expense")
#     Amount = st.number_input(label = "Please enter the amount you have spent")
#     Date = st.date_input("Date of Expense",value = date.today())
#     if st.button("Save"):
#         try:
#             with open(file_path,"r") as f:
#                 user_data = json.load(f)
#         except (FileNotFoundError,json.JSONDecodeError):
#             user_data = []
#         new_expense = {
#             "Category":Category,
#             "Amount":Amount,
#             "Date":str(Date)
#         }
#         user_data.append(new_expense)
#         with open(file_path,"w") as f:
#             json.dump(user_data,f,indent=4)
#         st.success(f"Saved: {Category} - {Amount} on {Date}")
# elif user_choice =="View Expenses":
#     st.subheader("These are your expenses")
#     try:
#         with open(file_path,'r') as file:
#             json_data = json.load(file)
#         if json_data:
#             df = pd.DataFrame(json_data)
#             st.dataframe(df)
#         else:
#             st.info("No expenses found.Add some first")
#     except FileNotFoundError:
#         st.warning("No expense file found. Please add an expense first!")
# elif user_choice =="Summary":
#     st.subheader("Expense Summary")
#     df = pd.read_json(file_path)
#     categories = df['Category']
#     values = df['Amount']
#     plt.bar(categories,values)
#     plt.xlabel('Category')
#     plt.ylabel('Amount spend')
#     plt.title('Expense Summary')
#     plt.xticks(rotation = 45)
#     plt.tight_layout()
#     st.pyplot(plt)
#weather app
#
# yet to be done
import streamlit as st
import requests
# # api_url = "http://api.openweathermap.org/data/2.5/weather"
# api_url = "http://api.openweathermap.org/geo/1.0/direct?q={city name},{state code},{country code}&limit={limit}&appid={API key}"
# api_key = "85e73ca1843f8b3f0790ba85302ca52d"
# st.title("Welcome to the Weather App")
# user_city = st.text_input(label = "Please enter your city")
# if st.button("Get Weather"):
#     if user_city:
#         geo_url = "http://api.openweathermap.org/geo/1.0/direct"
#         geo_params = {"q":user_city,"appid":api_key}
#         geo_response = requests.get(geo_url,geo_params)
#         if geo_response.status_code ==200 and geo_response.json():
#             lat = geo_response.json()[0]["lat"]
#             lon = geo_response.json()[0]["lon"]
#
#             #Step 2:Get 5-day forecast
#             forecast_url = "http://api.openweathermap.org/data/2.5/forecast"
#             forecast_params = {"lat":lat,"lon":lon,"appid":api_key,"units":"metric"}
#             forecast_response = requests.get(forecast_url,forecast_params)
#             if forecast_response.status_code == 200:
#                 forecast_data = forecast_response.json()
# crypto_api_key = "CG-qEuyWBpMTPZFjg2Pn5SaJNGw"
# api_url = "https://api.coingecko.com/api/v3/simple/price?ids=(str)&vs_currencies=usd&include_market_cap=true&include_24hr_change=true"
# coins_list_url = "https://api.coingecko.com/api/v3/coins/list"
# fig,ax = plt.subplots()
# st.title("Welcome to the Crypto King")
# st.header("We make you rich")
# crypto_list_response =requests.get(coins_list_url)
# crypto_data_list = []
# if crypto_list_response.status_code == 200:
#     crypto_data_list = crypto_list_response.json()   # This is a list of dicts
#     # Extract just the names
#     coin_names = [coin["name"] for coin in crypto_data_list]
# else:
#     coin_names = []
#
# # Show dropdown to user
# select_option = st.selectbox(
#     "Choose one coin and we will display the details:",
#     coin_names
# )
#
# st.write("You selected:", select_option)
# if st.button("Get Details of Coins"):
#     # Step 1: Map selected coin name back to its id
#     coin_id = None
#     for coin in crypto_data_list:
#         if coin["name"] == select_option:
#             coin_id = coin["id"]
#             break
#
#     if coin_id:
#         # Step 2: Use /simple/price endpoint
#         price_url = "https://api.coingecko.com/api/v3/simple/price"
#         params = {
#             "ids": coin_id,
#             "vs_currencies": "usd",
#             "include_market_cap": "true",
#             "include_24hr_change": "true"
#         }
#         response = requests.get(price_url, params=params)
#         if response.status_code == 200:
#             data = response.json()[coin_id]
#             # st.metric(label="Price (USD)",value = data["usd"]),
#             # st.metric(label = "Market Cap",value = data["usd_market_cap"]),
#             # st.metric(label="24h Change(%)",value= round(data["usd_24h_change"],2))
#             data_to_show = {
#                 "Metric": ["Price (USD)", "Market Cap", "24h Change (%)"],
#                 "Value": [data["usd"], data["usd_market_cap"], round(data["usd_24h_change"], 2)]
#             }
#             df = pd.DataFrame(data_to_show)
#             ax.bar(df["Metric"], df["Value"])
#             ax.set_xlabel("Metrics")
#             ax.set_ylabel("Values")
#             ax.set_title(f"Stats for {select_option}")
#             st.pyplot(fig)
#         else:
#             st.error("Error fetching coin details")
#     else:
#         st.error("Coin ID not found")

#
#News aggregator
from datetime import date

api_key_for_news = "ff32a5e849d242ab8defc7597c5629da"#
api_url = f"https://newsapi.org/v2/everything"#This lines handle the api part
st.title("Welcome to the Update")
st.header("We make you smarter everyday")#These two handle the titles for user to see
news_category = st.text_input("Please choose a topic like AI,Climate or Bitcoin")#user input
#now here the fun starts
if st.button(f"Get Updated on {news_category}"):# this is the button that will show the user the output
    if not news_category.strip():#this part is used if the user doesnt enter anything
        st.warning("Please enter a topic first")
    else:
        # you see that everything in the api_url,the params below are contained
        """
        Think of these as how you would sort the newspaper from frontpage to the full article on another page that's what the api_url does with these
        """
        params = {
            "q":news_category,
            "language":"en",
            "pageSize":20,
            "apikey":api_key_for_news
        }
        #this call below is made to the api after assigning the params it just says please use these directions and get this to me
        try:
            news_response = requests.get(api_url,params=params,timeout=10)
        #this will pop if the server is down or you dont have internet
        except requests.exceptions.RequestException as e:
            st.error(f"Network error:{e}")
        #if everything is good then this part works:
        else:
            if news_response.ok:
                data = news_response.json()#the data you see on newspaper is not like that its interpreted tested corrected  that's what json does for digital data
                articles = data.get("articles",[])#what does this line do?
                if articles:
                    for article in articles:
                        # the following part is just plain english
                        st.subheader(article["title"])
                        if article["urlToImage"]:
                            st.image(article["urlToImage"],width = 600)
                        st.write(article["description"])
                        st.write(f"[Read more]({article['url']})")
                        st.write("---")
                    #if what you want is not found then :
                else:
                    st.error(f"API error: {news_response.status_code} — {news_response.text}")

