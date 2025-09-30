import requests

def fetch_random_user_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()
    # print(data)

    if data["success"] and "data" in data:
        user_data = data["data"]
        user_name = user_data["login"]["username"]
        country = user_data["location"]["country"]
        return user_name, country
    
    else:
        raise Exception("Failed to fetch userdata")

def main():
    try:
       user_name, country =  fetch_random_user_freeapi()
       print(f"Username: {user_name}\nCountry: {country}")
    except Exception as e:
        print(str(e))
        # print("Error")

if __name__ == "__main__":
    main()