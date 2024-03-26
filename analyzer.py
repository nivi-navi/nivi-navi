import text as t

while True:
    text=input("Enter a piece of text:")
    print("\nchoose an option:")
    print("1.Calculate the number of words in the text.")
    print("2.Calculate the number of characters in the text.")
    print("3.Reverse the text.")
    print("4.Capitalize the text.")
    options=input("Enter your options(1/2/3/4):")
    if options=='1':
        wordcount=t.count_words(text)
        print('The number of words in this text:',wordcount)
    elif options=="2":
        charcount=len(text)
        print('The number of characters in this text:',charcount)
    elif options=="3":
        revText=t.reverse_text(text)
        print('The reversed text is: ',revText)
    elif options=="4":
        capText=t.capitalize_text(text)
        print('The capitalized text is :',capText)
    else:
        print("Exit")
        break
                        