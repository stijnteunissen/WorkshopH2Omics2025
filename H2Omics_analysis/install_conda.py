
def install_conda_and_packages():
    """
    Installs Conda and required Bioconda packages using shell commands.
    """
    # Install Conda
    !pip install -q condacolab
    import condacolab
    condacolab.install()

    # Install required Bioconda packages
    !conda install -q -c bioconda/label/cf201901 hmmer -y
    !conda install -q -c bioconda easel -y
    !conda install -q -c bioconda/label/cf201901 epa-ng -y

    print("Installation completed successfully!")
