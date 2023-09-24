def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    # Write your code here.
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort(reverse=fastest)
    total_speed = 0

    for idx in range(len(redShirtSpeeds)):
        red_speed = redShirtSpeeds[idx]
        blue_speed = blueShirtSpeeds[idx]

        total_speed += max(red_speed, blue_speed)

    return total_speed
