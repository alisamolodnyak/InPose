from datetime import datetime


def sort_by_season_and_location():
    seasons = [month % 12 // 3 + 1 for month in range(1, 13)]
    current_season = seasons[datetime.now().month - 1]
    print(current_season)


sort_by_season_and_location()


