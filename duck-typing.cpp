// duck-typing.cpp

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
