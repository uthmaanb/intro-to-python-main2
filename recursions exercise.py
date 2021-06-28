# define function.
def fibonacci(x):
    # return 1 and 0 because there is not two numbers before them.
    if x == 0:
        return 0
    if x == 1:
        return 1
    else:
        # the equation for fibonacci numbers ( f(n) = f(n-1) + f(n-2) ).
        return fibonacci(x-1) + fibonacci(x-2)


# set range to 21 because we want the sequence till 20.
x = range(21)

print("Fibonacci sequence till 20: ")
for n in x:
    print(fibonacci(n))








def ibmi_calc():
    if option == "Male":
        weight = float(w_input.get())
        height = float(h_input.get())
        bmi_m_ans = 0.5 * weight / (height / 100) * 2 + 11.5
        ibmi.set(bmi_m_ans)

    elif option == "Female":
        weight = float(w_input.get())
        height = float(h_input.get())
        age = float(a_input.get())
        bmi_f_ans = 0.5 * weight / (height / 100) * 2 + 0.03 * age + 11
        ibmi.set(bmi_f_ans)


# def bmi calculation
def bmi_calc():
    weight = float(w_input.get())
    height = float(h_input.get())
    bmi_ans = weight / height**2
    bmi.set(bmi_ans)


def calc():
    ibmi_calc()
    bmi_calc()


def act_age():
    if entry3['state'] == DISABLED:
        entry3.config(state="normal")