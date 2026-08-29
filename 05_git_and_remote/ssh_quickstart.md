# SSH quickstart

SSH opens an encrypted shell on another computer. The workshop may use it to access remote compute. Use the actual hostname, username, and authentication instructions supplied by CV4Ecology instructors.

## First login

From a terminal on your **local computer**:

```bash
ssh YOUR_USERNAME@WORKSHOP_HOSTNAME
```

On a first connection, SSH may show the server's fingerprint. Verify it against information supplied by the instructors before accepting it.

After login, the prompt normally changes. These commands now run on the **remote computer**:

```bash
hostname
pwd
ls
```

Return to your local computer with:

```bash
exit
```

Run `hostname` or `pwd` again locally if you are unsure which machine you are using.

## Optional small-file transfer

From the terminal in your local computer:

```bash
scp path/to/small_test_file YOUR_USERNAME@WORKSHOP_HOSTNAME:destination/path/
```

The colon after the hostname is important: it separates the remote host from the path on that host.

Do not test with a full dataset until you decide on a subset with your instructors.

## SSH key safety

- A public key usually ends in `.pub` and may be shared with the service that needs it.
- A private key does not end in `.pub`; never email it, upload it, commit it, or show its contents.
- Use the key type, passphrase, and registration process specified by the workshop platform.
- GitHub SSH authentication and SSH login to workshop compute may use similar technology but are separate configurations.

For GitHub authentication, use [GitHub's SSH documentation](https://docs.github.com/en/authentication/connecting-to-github-with-ssh).

## Extra reading
For the current general workflow, see [HPC Carpentry's remote connection lesson](https://carpentries-incubator.github.io/hpc-intro/11-connecting.html). 
