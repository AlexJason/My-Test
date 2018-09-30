#include <iostream>
#include <vector>
#include <fstream>

#include <boost/progress.hpp>

using namespace std;
using namespace boost;

int main() {
	vector<string> v(100);
	ofstream fs("./test.txt");

	progress_display pd(v.size());
	int pos = 0;

	for (auto&x : v) {
		fs << x << endl;
		pd.restart(v.size());
		pd += ++pos;
	}

	system("pause");
	return 0;
}
