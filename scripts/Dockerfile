# The purpose of this docker file is to provide a shell with
# hive-python pre-installed for interactive testing purposes.
#
# Usage:
# docker build -t hivepy .
# docker run -it hivepy

FROM python:3.5.3
MAINTAINER pharesim <pharesim@protonmail.com>

# set default password for BIP38 encrypted wallet
ENV UNLOCK test123

RUN pip install ipython
RUN pip install git+git://github.com/pharesim/hive-python.git

CMD "ipython"
