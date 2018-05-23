# Duck typing

- https://en.wikipedia.org/wiki/Duck_typing
> In computer programming, duck typing is an application of the duck test in type safety. It requires that type checking be deferred to runtime, and is implemented by means of dynamic typing or reflection.
Duck typing is concerned with establishing the suitability of an object for some purpose, using the principle, <b>"If it walks like a duck and it quacks like a duck, then it must be a duck."</b> With normal typing, suitability is assumed to be determined by an object's type only. In duck typing, an object's suitability is determined by the presence of certain methods and properties (with appropriate meaning), rather than the actual type of the object.
- https://stackoverflow.com/questions/4205130/what-is-duck-typing
> It is a term used in [dynamic languages](http://en.wikipedia.org/wiki/Dynamic_programming_language) that do not have [strong typing](http://en.wikipedia.org/wiki/Strong_typing).
The idea is that you don't need a type in order to invoke an existing method on an object - if a method is defined on it, you can invoke it.
The name comes from the phrase "If it looks like a duck and quacks like a duck, it's a duck".
[Wikipedia](https://en.wikipedia.org/wiki/Duck_typing) has much more information.
- https://medium.com/@matryer/golang-advent-calendar-day-one-duck-typing-a513aaed544d
- https://gist.github.com/khajavi/03823f934c5291ae7cd1a83479eedbc6
- https://ko.wikipedia.org/wiki/%EB%8D%95_%ED%83%80%EC%9D%B4%ED%95%91

```python
# duck-typing.py
class Parrot:
	def fly(self):
		print("Parrot flying")

class Airplane:
	def fly(self):
		print("Airplane flying")

class Whale:
	def swim(self):
		print("Whale swimming")

def lift_off(entity):
	entity.fly()

parrot = Parrot()
airplane = Airplane()
whale = Whale()

lift_off(parrot) # prints `Parrot flying`
lift_off(airplane) # prints `Airplane flying`
lift_off(whale) # Throws the error `'Whale' object has no attribute 'fly'`
```

```go
// duck-typing.go
package main

import "fmt"

type Speaker interface {
        Say(string)
}

type Person struct {
        name string
}

func (p *Person) Say(message string) {
        fmt.Println(p.name + ":" , message)
}

func SpeakAlphabet(via Speaker) {
        via.Say("abcdefgh")
}

func main() {
        mat := new(Person)
        mat.name = "Mat"
        SpeakAlphabet(mat)
}
```

```cpp
class Duck {
public:
    void quack() {
        std::cout << "Quaaaaaack!" << std::endl;
    }
    
    void feathers() {
        std::cout << "The duck has white and gray feathers." << std::endl;
    }
}

class Person {
public:
    void quack() {
        std::cout << "The person imitates a duck." << std::endl;
    }
    
    void feathers() {
        std::cout << "The person takes a feather from the ground and shows it." << std::endl;
    }
}

template <typename T>
void inTheForest(T& t)
{
    t.quack();
    t.feathers();
}

int main()
{
    Duck donald;
    Person jhon;
    
    inTheForest( donald );
    inTheForest( jhon );
}
```
