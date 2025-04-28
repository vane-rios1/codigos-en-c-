#include <iostream>
using namespace std;

int main() {
    int base, altura, area;

    cout << "¡Hola!" << endl;
    cout << "Ingrese la base del triangulo: ";
    cin >> base;

    cout << "Ingrese la altura del triangulo: ";
    cin >> altura;

    area = base * altura / 2;

    cout << "La base del triangulo es de " << base << ", la altura del triangulo es de " << altura << ", su area es de " << area << endl;

    return 0;
}
