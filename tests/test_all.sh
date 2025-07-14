# run all test files but exit at first failure
for FILE in test_*.py;do
pytest $FILE
if [[ $? != 0 ]] ; then exit 1 ; fi
done
echo "*** All tests succeeded"