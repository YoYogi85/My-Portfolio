loan_amount =int (input ('Amount Borrowed? '))
interest_rate = float (input ('What is the APR? '))
duration = int (input ('What is the term in years? '))

term = duration * 12
interest = interest_rate / 1200
monthly = round (loan_amount * ((interest * ((interest + 1) ** term)) / 
          (((interest + 1) ** term) - 1)), 2) 
life = round (monthly * term, 2) 


print ('Your monthly payments will be: £', monthly)
print ('Your total amount payable will be: £', life)
