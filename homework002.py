# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# для всех значений предикат.

X=(True,False)
Y=(True,False)
Z=(True,False)
for i in X:
    for j in Y:
        for k in Z:
            print(f'¬({X[i]} ⋁ {Y[j]} ⋁ {Z[k]}) = ¬{X[i]} ⋀ ¬{Y[j]} ⋀ ¬{Z[k]}' )
            print(not (X[i] or Y[j] or Z[k])== (not X[i]) and (not Y[j]) and (not Z[k]))