def dsj_topic():
    print("Hiring Practices Experience Survey")
response = input("Have you experienced discrimination when looking for a job? (yes/no): ")
if response.lower() == "yes":
    print("Thank you for sharing.")
    details = input("Then I have a book for you if you're interested. It's called Stories employers Tell by Phillip Moss and Chris Tilly: ")
else: 
        print("Then you are very fortunate.")
