scores={"Bob":96,"Alice":90,"Mary":79,"John":80,"Elon":68}
std_name=input("Enter the student's name: ")
if std_name not in scores:
    print(f"{std_name} is not found in the dictionary")
else:
    print(f"{std_name}'s marks: {scores[std_name]}")