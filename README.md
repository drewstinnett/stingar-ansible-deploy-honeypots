# stingar-ansible-deploy-honeypots

These are ansible scripts meant to be deployed from a STINGAR control host.

# Hacky getting Started

Populate elasticsearch with some data using:

```
./scripts/dummy_es_data.py
```

You can manually run the playbook until the automation button is in place with:

```
ansible-playbook -i $COWRIE_SERVER_IP, ./deploy_cowrie.yaml  --extra-vars="target=$COWRIE_SERVER_IP"
```
