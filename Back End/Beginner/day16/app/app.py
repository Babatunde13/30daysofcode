from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1> Welcome to my #30daysofcode back end challenge</h1>'

def is_prime(n):
    for i in range(2,int(n**0.5)+1):
        if n % i == 0: return False
    return True

def sievePrime(n):
    primes = [i for i in range(2, n+1)]
    i = 2
    while i <= int(n**0.5):
        if i in primes:
            for j in range(i*2, n+1, i):
                if j in primes:
                    primes.remove(j)
        i+=1
    pr = [str(i)+', ' for i in primes]
    pr[-2:]= [pr[-2][:-2]+' and ', pr[-1][:-2]]
    return ''.join(pr)
    
@app.route('/primes/')
def primes():
    prime = sievePrime(74)
    return f'<h1>The first 20 prime numbers are: {prime} </h1>'
# print(primes())

if __name__ == "__main__":
    app.run(debug=False)
