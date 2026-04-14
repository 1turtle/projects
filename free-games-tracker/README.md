# FreeGamesTracker
## Overview
This website shows free video games from select markets. Potential new free
video games are updated every Thursday at 17:00 UTC unless due to special
events. In this website, free video games are defined as paid video games doing
a free-to-keep promotion basically meaning a 100% discount sale.

## Markets
- [Steam](https://store.steampowered.com/) and [SteamDB](https://steamdb.info/)
- [Epic Games](https://store.epicgames.com/en-US)
- [GOG Games](https://www.gog.com/en/)
- [PlayStation Plus (Subscription)](https://store.playstation.com/en-us/view/25d9b52a-7dcf-11ea-acb6-06293b18fe04/bc428b4a-f1b7-11ea-aadc-062143ad1e8d)
- [Amazon Prime Gaming (Subscription)](https://gaming.amazon.com/home)

## Description
View the website [here](https://freegamestracker.netlify.app/).

Or you can view ```data.json``` located in ```./src/resources/``` to see the
data manually. ```test_data.json``` and ```empty.json``` are only used for
developmental purposes.

## Tools
- React
- Selenium
- GitHub Actions CI/CD
- [CheapShark API](https://apidocs.cheapshark.com/#intro)

## Notes
CheapShark API provides free information like deals on video games with no sign
up required. However, any new video game release will take at least a few days to
show up in the CheapShark database meaning that the api may not have any data
to that game. Also, since the data was retrieved from various sources, image
quality and layout will defer. For the best viewing purposes, I recommend a
device size of at least 1020px.

## Contribution
- Established on August 2025 by 1turtle
