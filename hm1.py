lecture = int(input("enter lecture cnt: "))
attendencee = int(input("enter attendendce cnt: "))

x = (lecture - attendencee) / lecture

result = "accepted"
if x > 0.75:
    result = "forbidden"

print(result)