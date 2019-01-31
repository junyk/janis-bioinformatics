from bioinformatics.janis_bioinformatics.tools import BcfTools_1_5
from bioinformatics.janis_bioinformatics.tools.bcftools.norm.base import BcfToolsNormBase


class BcfToolsNorm_1_5(BcfTools_1_5, BcfToolsNormBase):
    pass


if __name__ == "__main__":
    print(BcfToolsNorm_1_5().help())