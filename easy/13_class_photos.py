def classPhotos(redShirtHeights, blueShirtHeights):
    # Write your code here.
    redShirtHeights.sort()
    blueShirtHeights.sort()
    is_red_shorter = False

    for idx, red_height in enumerate(redShirtHeights):
        if idx == 0:
            is_red_shorter = red_height < blueShirtHeights[0]

        if red_height == blueShirtHeights[idx]:
            return False

        if is_red_shorter and red_height > blueShirtHeights[idx]:
            return False
        elif is_red_shorter is False and blueShirtHeights[idx] > red_height:
            return False

    return True
