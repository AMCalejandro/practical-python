# mortgage.py
#
# Exercise 1.7

# mortgage.py

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0

extra_payment_start_month = int(input('Enter the start month for the extra payment:'))
extra_payment_end_month = int(input('Enter the end month for the extra payment:'))
extra_payment =  int(input('Enter the quantity of the extra payment:'))


while (principal > 0):
    month = month + 1

    if (month >= extra_payment_start_month) & (month <= extra_payment_end_month):
        if (principal * (1+rate/12)) <= (payment + extra_payment):
            last_payment = principal * (1+rate/12)
            principal = last_payment - last_payment
            total_paid = total_paid + principal
        else:
            principal = principal * (1+rate/12) - (payment + extra_payment)
            total_paid = total_paid + payment + extra_payment
    else:
        if (principal * (1+rate/12)) <= payment:
            last_payment = principal * (1+rate/12)
            principal = last_payment - last_payment
        else:
            principal = principal * (1+rate/12) - payment
            total_paid = total_paid + payment

    print(f'{month} {total_paid:0.4f} {principal:0.4f}')

print(f'\nTotal paid {total_paid:0.4f} months required {month:0.4f}')
