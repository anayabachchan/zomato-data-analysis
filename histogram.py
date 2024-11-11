plt.figure(figsize=(10,6))
plt.hist(data['rating'], bins=10, color='skyblue')
plt.title('Histogram of Ratings')
plt.xlabel('Ratings')
plt.ylabel('Frequency')
plt.show()
