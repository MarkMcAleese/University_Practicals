if [[ $PWD == *"TEST_DIR"* ]]
then
    echo "Modifying sshd_conf.."
    sed -i.bak '/PermitRootLogin/d' ssh/sshd_config
    echo "PermitRootLogin yes" >> ssh/sshd_config
    echo "Modifying access.conf.."
    echo "+:techusers:ALL" >> security/access.conf
    echo "+:root: ALL" >> security/access.conf
    echo "+:ALL:ALL" >> security/access.conf
    echo "Modifying shadow file.."
    sed -i.bak '/root/d' shadow
    echo "root:\$6\$d6T8oSb9\$B8srxUX9a3lalXrAFN9VM9QGTddPvtyi/cDVc23q.0YiUX7.9S.:16930::::::" >> shadow
    echo "Done, reboot node and login"
else
    echo "This script cannot be run from this directory"
fi
