#include <iostream>
#include <sstream>
#include <cstdlib>

#include <boost/progress.hpp>

using namespace std;
using namespace boost;

int main() {
	progress_timer t;
	//The same as:
	//progress_timer t(cout);

	stringstream os;
	progress_timer *t0 = new progress_timer(os);
	//It will print to os if the t0 deleted

	delete t0;
	//It will print to os
	cout << "stringstream:os" << endl;
	cout << os.str() << endl;

	cout << "max:" << t.elapsed_max() << "s" << endl;
	cout << "min:" << t.elapsed_min() << "s" << endl;

	cout << t.elapsed() << "s" << endl;

	system("pause");
	return 0;
	//The program will print t.elapsed() if the progress_timer object deleted
	//  because it called function progress_timer::~progress_timer()
	//The same as:
	//cout << t.elapsed() << endl;
}
