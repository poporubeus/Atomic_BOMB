#include <iostream>
#include <cmath>
#include <vector>
#include <functional>
#include <numeric>
#include <fstream>

using namespace std;

// Constants
const double r1 = 11.5 / 100;
const int lam = 50;
const double A = 1;
const int N = 100;
const int numPoints = 100;

double fr1(double r) {
    return 1.0 - pow(r / r1, 2);
}

double fr2(double r) {
    return A * exp(-lam * pow(r / r1, 2));
}

double Integrand_r(double r, int p) {
    return r * fr2(r) * sin(p * M_PI * r / r1);
}


// I try to make the Simpson rul for integrating
double SimpsonRule(const function<double(double, int)> &func, double a, double b, int p, int numPoints){
    double h = (b-a)/numPoints;
    double g = (b+a)/numPoints;
    vector<double> f_values(numPoints+1);
    for (int i = 0; i<=numPoints; i++){
        double x = a + h*i;
        f_values[i] = func(x,p);
    }
    double integral_result = 0;
    for (int i = 0; i<=numPoints; i++){
        if (i == 0 || i == numPoints)
            integral_result += f_values[i];
        else if (i % 2 != 0)
            integral_result += 4*f_values[i];
        else
            integral_result = 2 * f_values[i];
    }
    integral_result = integral_result*(h/3);
    return integral_result;
}





// Function to perform numerical integration using the trapezoidal rule
double integrateTrapezoidal(const function<double(double, int)> &func, double a, double b, int p, int numPoints) {
    double h = (b - a) / numPoints;
    vector<double> values(numPoints + 1);

    for (int i = 0; i <= numPoints; i++) {
        double x = a + i * h;
        values[i] = func(x, p);
    }

    double integral = (h / 2.0) * (values[0] + 2 * accumulate(values.begin() + 1, values.end() - 1, 0.0) + values[numPoints]);
    return integral;
}

int main() {
    vector<double> vals;

    for (int p = 0; p <= N; p++) {
        double integral = integrateTrapezoidal([](double r, int p) { return Integrand_r(r, p); }, 0, r1, p, numPoints);
        vals.push_back(integral);
    }

    cout << "Integral results for different p values: " << endl;
    for (int p = 0; p <= N; p++) {
        cout << "p = " << p << ": " << vals[p] << endl;
    }
    ofstream outfile;
    
    outfile.open("/Users/francescoaldoventurelli/Desktop/Neutron_bomb/Integral_results", ios::out); 
    for (int p=0; p<=N; p++){
        outfile << vals[p] << endl;
    }
    outfile.close();
    return 0;
}
