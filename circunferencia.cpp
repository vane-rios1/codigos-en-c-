#include <iostream>
using namespace std;

int main() {
    int radio;
    float circunferencia;

    cout << "¡Hola!" << endl;
    cout << "Ingrese el radio del circulo: ";
    cin >> radio;

    circunferencia = 2 * 3.1416 * radio;

    cout << "El radio del circulo es de " << radio << ", el perimetro de la circunferencia es de " << circunferencia << endl;

    return 0;
}
