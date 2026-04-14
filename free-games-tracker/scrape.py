import json, requests, re, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

EPIC_URL = "https://store.epicgames.com/en-US"
EPIC_API = "https://www.cheapshark.com/api/1.0/deals?storeID=25"
PS_PLUS_URL = "https://www.playstation.com/en-us/ps-plus/whats-new/"
AMZ_PRI_URL = "https://gaming.amazon.com/home"
STEAM_API = "https://www.cheapshark.com/api/1.0/deals?storeID=1"
GOG_API = "https://www.cheapshark.com/api/1.0/deals?storeID=7"
# 1: Steam, 7: GoG, and 25: Epic Games

data = []



# This function below has a chance to trigger a checkbox CAPTCHA verification.
#def scrape_epic(driver):
#    try:
#        print("[SYSTEM]: Selenium running on Epic Games.")
#        driver.get(EPIC_URL)
#        time.sleep(3)
#        epic_games_section = driver.find_element(By.CLASS_NAME, "css-1myhtyb")
#        epic_games = epic_games_section.find_elements(By.CLASS_NAME, "css-g3jcms")
#        for epic_game in epic_games:
#            epic_game_link = epic_game.get_attribute("href")
#            epic_game_title = epic_game.find_element(By.CSS_SELECTOR, ".eds_1ypbntd0.eds_1ypbntd7.eds_1ypbntdq").text
#            epic_game_id = epic_game_link.replace("https://store.epicgames.com/en-US/p/", "").strip().lower()
#            epic_game_img = epic_game.find_element(By.TAG_NAME, "img").get_attribute("data-image")
#            epic_game_status = epic_game.find_element(By.CSS_SELECTOR, ".css-82y1uz, .css-gyjcm9").text.strip().replace(" ", "_").lower()
#        
#            if epic_game_status == "free_now":
#                data.append({"title": epic_game_title, "id": epic_game_id, "img": epic_game_img, "link": epic_game_link, "market": "epic_games"})
#
#        print("[SYSTEM]: Selenium has finished on Epic Games.")
#    
#    except Exception as e:
#        print(f"[SYSTEM]: Selenium has FAILED on Epic Games. Reason: {e}.")



def scrape_ps(driver):
    try:
        print("[SYSTEM]: Selenium running on PlayStation.")
        offset = 1
        driver.get(PS_PLUS_URL)
        time.sleep(3)
        
        #ps_plus_games_section = driver.find_element(By.XPATH, "//*[@id='monthly-games']/div/div/div")
        ps_plus_games = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "box--light")))
        for ps_plus_game in ps_plus_games:
            ps_plus_game_link = ps_plus_game.find_element(By.XPATH,
                                                          "//*[@id='monthly-games']/div/div/div/div["
                                                          + str(offset) + "]/div[2]/div/div[2]/a").get_attribute("href")
            ps_plus_game_id = ps_plus_game_link.replace("https://www.playstation.com/en-us/games/", "").strip().lower()
            end_char = ps_plus_game_id.index("/")
            ps_plus_game_id = ps_plus_game_id[:end_char]
            ps_plus_game_img = ps_plus_game.find_element(By.XPATH, "//*[@id='monthly-games']/div/div/div/div[" + str(offset) + "]/div[1]/div/div/figure/picture/source[1]").get_attribute("srcset")
            ps_plus_game_title = ps_plus_game.find_element(By.XPATH, "//*[@id='monthly-games']/div/div/div/div[" + str(offset) + "]/div[2]/div/div[1]/h3").text
            data.append({"title": ps_plus_game_title, "id": ps_plus_game_id, "img": ps_plus_game_img, "link": ps_plus_game_link, "market": "playstation"})
            offset+=1
    
        print("[SYSTEM]: Selenium has finished on PlayStation.")

    except Exception as e:
        print(f"[SYSTEM]: Selenium has FAILED on PlayStation. Reason: {e}.")



def scrape_amz_pri(driver):
    try:
        print("[SYSTEM]: Selenium running on Prime Gaming.")
        offset = 1
        driver.get(AMZ_PRI_URL)
        time.sleep(3)
        
        for _ in range(10):
            driver.find_element(By.ID, ("root")).send_keys(Keys.PAGE_DOWN)
            time.sleep(1)
        
        prime_games_section = driver.find_element(By.XPATH, "//*[@id='offer-section-FGWP_FULL']/div[2]/div")
        prime_games = prime_games_section.find_elements(By.CLASS_NAME, "item-card__action");
        
        for prime_game in prime_games:
            load_prime_game_link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='offer-section-FGWP_FULL']/div[2]/div/div[" + str(offset) + "]/div/div/div/a")))
            prime_game_link = load_prime_game_link.get_attribute("href")
            prime_game_id = prime_game_link.replace("https://gaming.amazon.com/", "").strip().lower()
            end_char = prime_game_id.index("/")
            prime_game_id = prime_game_id[:end_char]
            prime_game_img = prime_game.find_element(By.TAG_NAME, "img").get_attribute("src")
            prime_game_title = prime_game.find_element(By.TAG_NAME, "a").get_attribute("aria-label")
            prime_game_title = load_prime_game_link.get_attribute("aria-label")
            data.append({"title": prime_game_title, "id": prime_game_id, "img": prime_game_img, "link": prime_game_link, "market": "amazon"})
            offset+=1

        print("[SYSTEM]: Selenium has finished on Prime Gaming.")

    except Exception as e:
        print(f"[SYSTEM]: Selenium has FAILED on Prime Gaming. Reason: {e}.")



def fetch_epic():
    try:
        print("[SYSTEM]: Fetching Epic API...")
        response = requests.get(EPIC_API)
        epic_data = response.json()
        for game in epic_data:
            if float(game["salePrice"]) == 0 and float(game["savings"]) == 100:
            #if float(game["salePrice"]) > 0:
                epic_game_id = game["steamAppID"]
                #epic_game_link = "http://store.steampowered.com/app/" + str(epic_game_id) + "/"
                epic_game_link = f"https://www.cheapshark.com/redirect?dealID={game['dealID']}"
                data.append({"title": game["title"], "id": epic_game_id, "img": game["thumb"], "link": epic_game_link, "market": "epic_games"})

        print("[SYSTEM]: Done with Epic API.")
    
    except Exception as e:
        print(f"[SYSTEM]: Failed to fetch Epic API... Reason: {e}.")



def fetch_steam():
    try:
        print("[SYSTEM]: Fetching Steam API...")
        response = requests.get(STEAM_API)
        steam_data = response.json()
        for game in steam_data:
            if float(game["salePrice"]) == 0 and float(game["savings"]) == 100:
            #if float(game["salePrice"]) > 0:
                steam_game_id = game["steamAppID"]
                steam_game_link = "http://store.steampowered.com/app/" + str(steam_game_id) + "/"
                data.append({"title": game["title"], "id": steam_game_id, "img": game["thumb"], "link": steam_game_link, "market": "steam"})

        print("[SYSTEM]: Done with Steam API.")
    
    except Exception as e:
        print(f"[SYSTEM]: Failed to fetch Steam API... Reason: {e}.")
    


def fetch_gog():
    try:
        print("[SYSTEM]: Fetching GOG API...")
        response = requests.get(GOG_API)
        gog_data = response.json()
        for game in gog_data:
            if float(game["salePrice"]) == 0 and float(game["savings"]) == 100:
            #if float(game["salePrice"]) > 0:
                gog_game_id = re.sub(r'[^a-zA-Z0-9\s]', '', game["title"])
                gog_game_id = re.sub(r'\s+', '_', gog_game_id)
                gog_game_link = "https://www.gog.com/en/game/" + str(gog_game_id) + "/"
                data.append({"title": game["title"], "id": gog_game_id, "img": game["thumb"], "link": gog_game_link, "market": "gog"})

        print("[SYSTEM]: Done with GOG API.")
    
    except Exception as e:
        print(f"[SYSTEM]: Failed to fetch GOG API... Reason: {e}.")



def scrape_all():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(options=options)
    scrape_ps(driver)
    time.sleep(1)
    scrape_amz_pri(driver)
    time.sleep(1)
    driver.close()



def fetch_all():
    fetch_epic()
    time.sleep(1)
    fetch_steam()
    time.sleep(1)
    fetch_gog()



def main():
    print("[SYSTEM]: Scraping has started.")

    scrape_all()
    fetch_all()

    with open("./src/resources/data.json", "w") as file:
        json.dump(data, file, indent=4)

    print("[SYSTEM]: Scraping is complete.")



if __name__ == "__main__":
    main()
