PKG=python-rpmbuild-chain
VER=0.9

all: rpm

test:
	python2 setup.py nosetests
	python3 setup.py nosetests

integ:
	tests/integ_test.sh

srpm: clean
	mkdir -p rpmbuild/SOURCES
	tar --exclude-vcs --exclude='./rpmbuild' --transform "s;^./;${PKG}-${VER}/;" \
		-zcvf rpmbuild/SOURCES/${PKG}-${VER}.tar.gz ./
	rpmbuild --define "_topdir $(shell pwd)/rpmbuild/" --undefine "dist" \
		-bs ${PKG}.spec

rpm: srpm
	rpmbuild --define "_topdir $(shell pwd)/rpmbuild/" \
		--rebuild rpmbuild/SRPMS/${PKG}-${VER}-*.src.rpm

clean:
	rm -rf rpmbuild dist build *.egg-info .coverage
	find . -type d -name "__pycache__" -prune -exec rm -rf {} \;
	find . -type f -name "*.pyc" -delete
