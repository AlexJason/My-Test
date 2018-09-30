#include <iostream>

#include <boost/timer.hpp>

using namespace std;
using namespace boost;

int main() {
	timer t;
	
	cout << "max timespan:"
		<< t.elapsed_max() / 3600 << "h" << endl;
	//The maxinum time

	cout << "min timespan:"
		<< t.elapsed_min() << "s" << endl;
	//The mininum time

	cout << "now time elapsed:"
		<< t.elapsed() << "s" << endl;
	//The time elapsed from the object created

	system("pause");
	return 0;
}
