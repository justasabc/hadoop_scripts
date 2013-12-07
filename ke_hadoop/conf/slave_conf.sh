# on master node
cd .
cp ./slave_node/* ../../hadoop/conf/
echo "conf/masters"
cat ../../hadoop/conf/masters
echo "conf/slaves"
cat ../../hadoop/conf/slaves
