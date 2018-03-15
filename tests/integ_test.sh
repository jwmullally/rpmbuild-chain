#!/bin/sh
set -ex

echo "Running test build..."

rm -rf build/integ/
sudo rm -f /etc/yum.repos.d/rpmbuild-chain.repo
sudo rpm -e pkg{A,B,C} || true
for f in tests/specs/standard/*; do
	rpmbuild --define "_topdir $(pwd)/build/integ/input" -bs $f
done
sudo python -m rpmbuild_chain --verbose --user $USER --repo-path build/integ/output --hookdir tests/hookdir --lint --srpms build/integ/input/SRPMS/pkg*.src.rpm

cd build/integ/output
for pkg in pkg{A,B,C,D,E}; do
    cd ${pkg}-1.0-1
    [ -f ${pkg}-1.0-1.noarch.rpm ]
    [ -f ${pkg}-1.0-1.src.rpm ]
    [ -f build.log ]
    [ -f installed_pkgs.log.gz ]
    [ -f ${pkg}.spec ]
    [ -f ${pkg}.spec.parsed ]
    [ -f pre_build.test ]
    [ -f post_build.test ]
    [ -f rpmlint.log ]
    [ -f success ]
    cd ..
done
[ -f pre_run.test ]
[ -f post_run.test ]

echo "All tests passed"
