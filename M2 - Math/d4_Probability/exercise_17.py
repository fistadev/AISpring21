# Calculate the probability of drawing a heart or an ace
heart = 13/52
ace = 4/52
# remove intersection, so it doesn't add twice
prob = (heart + ace) - heart * ace
print(round(prob, 3))
