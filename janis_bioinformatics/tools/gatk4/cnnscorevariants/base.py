from abc import ABC
from datetime import datetime

from janis_unix import JsonFile

from janis_bioinformatics.data_types import FastaWithDict, Vcf, VcfTabix
from janis_bioinformatics.tools.gatk4.gatk4toolbase import Gatk4ToolBase

from janis_core import (
    CommandTool,
    ToolInput,
    ToolOutput,
    File,
    Boolean,
    String,
    Int,
    Double,
    Float,
    InputSelector,
    Filename,
    ToolMetadata,
    InputDocumentation,
    Array,
)


class GatkCNNScoreVariantsBase(Gatk4ToolBase, ABC):
    @classmethod
    def gatk_command(cls):
        return "CNNScoreVariants"

    def friendly_name(self) -> str:
        return "GATK4: CNNScoreVariants"

    def tool(self) -> str:
        return "Gatk4CNNScoreVariants"

    def inputs(self):
        return [
            ToolInput(
                tag="outputFilename",
                input_type=Filename(
                    prefix=InputSelector("variant"),
                    suffix=".scored",
                    extension=".vcf.gz",
                ),
                prefix="--output",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="(-O) Output file Required."),
            ),
            ToolInput(
                tag="reference",
                input_type=FastaWithDict(optional=True),
                prefix="--reference",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="(-R) Reference sequence file Required."),
            ),
            ToolInput(
                tag="variant",
                input_type=Vcf(optional=True),
                prefix="--variant",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-V) A VCF file containing variants Required."
                ),
            ),
            ToolInput(
                tag="addOutputSamProgramRecord",
                input_type=Boolean(optional=True),
                prefix="--add-output-sam-program-record",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-add-output-sam-program-record)  If true, adds a PG tag to created SAM/BAM/CRAM files.  Default value: true. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="addOutputVcfCommandLine",
                input_type=Boolean(optional=True),
                prefix="--add-output-vcf-command-line",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-add-output-vcf-command-line)  If true, adds a command line header line to created VCF files.  Default value: true. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="architecture",
                input_type=JsonFile(optional=True),
                prefix="--architecture",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-architecture)  Neural Net architecture configuration json file  Default value: null. "
                ),
            ),
            ToolInput(
                tag="arguments_file",
                input_type=Array(File, optional=True),
                prefix="--arguments_file",
                separate_value_from_prefix=True,
                prefix_applies_to_all_elements=True,
                doc=InputDocumentation(
                    doc="read one or more arguments files and add them to the command line This argument may be specified 0 or more times. Default value: null. "
                ),
            ),
            ToolInput(
                tag="cloudIndexPrefetchBuffer",
                input_type=Int(optional=True),
                prefix="--cloud-index-prefetch-buffer",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-CIPB)  Size of the cloud-only prefetch buffer (in MB; 0 to disable). Defaults to cloudPrefetchBuffer if unset.  Default value: -1. "
                ),
            ),
            ToolInput(
                tag="cloudPrefetchBuffer",
                input_type=Int(optional=True),
                prefix="--cloud-prefetch-buffer",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-CPB)  Size of the cloud-only prefetch buffer (in MB; 0 to disable).  Default value: 40. "
                ),
            ),
            ToolInput(
                tag="createOutputBamIndex",
                input_type=Boolean(optional=True),
                prefix="--create-output-bam-index",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-OBI)  If true, create a BAM/CRAM index when writing a coordinate-sorted BAM/CRAM file.  Default value: true. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="createOutputBamMd5",
                input_type=Boolean(optional=True),
                prefix="--create-output-bam-md5",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-OBM)  If true, create a MD5 digest for any BAM/SAM/CRAM file created  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="createOutputVariantIndex",
                input_type=Boolean(optional=True),
                prefix="--create-output-variant-index",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-OVI)  If true, create a VCF index when writing a coordinate-sorted VCF file.  Default value: true. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="createOutputVariantMd5",
                input_type=Boolean(optional=True),
                prefix="--create-output-variant-md5",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-OVM)  If true, create a a MD5 digest any VCF file created.  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="disableBamIndexCaching",
                input_type=Boolean(optional=True),
                prefix="--disable-bam-index-caching",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-DBIC)  If true, don't cache bam indexes, this will reduce memory requirements but may harm performance if many intervals are specified.  Caching is automatically disabled if there are no intervals specified.  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="disableReadFilter",
                input_type=String(optional=True),
                prefix="--disable-read-filter",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-DF)  Read filters to be disabled before analysis  This argument may be specified 0 or more times. Default value: null. Possible Values: {ReadGroupBlackListReadFilter, WellformedReadFilter}"
                ),
            ),
            ToolInput(
                tag="disableSequenceDictionaryValidation",
                input_type=Boolean(optional=True),
                prefix="--disable-sequence-dictionary-validation",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-disable-sequence-dictionary-validation)  If specified, do not check the sequence dictionaries from our inputs for compatibility. Use at your own risk!  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="excludeIntervals",
                input_type=Boolean(optional=True),
                prefix="--exclude-intervals",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-XL) This argument may be specified 0 or more times. Default value: null. "
                ),
            ),
            ToolInput(
                tag="filterSymbolicAndSv",
                input_type=Boolean(optional=True),
                prefix="--filter-symbolic-and-sv",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-filter-symbolic-and-sv)  If set will filter symbolic and and structural variants from the input VCF  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="gatkConfigFile",
                input_type=String(optional=True),
                prefix="--gatk-config-file",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="A configuration file to use with the GATK. Default value: null."
                ),
            ),
            ToolInput(
                tag="gcsMaxRetries",
                input_type=Int(optional=True),
                prefix="--gcs-max-retries",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-gcs-retries)  If the GCS bucket channel errors out, how many times it will attempt to re-initiate the connection  Default value: 20. "
                ),
            ),
            ToolInput(
                tag="gcsProjectForRequesterPays",
                input_type=String(optional=True),
                prefix="--gcs-project-for-requester-pays",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Project to bill when accessing 'requester pays' buckets. If unset, these buckets cannot be accessed.  Default value: . "
                ),
            ),
            ToolInput(
                tag="help",
                input_type=Boolean(optional=True),
                prefix="--help",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-h) display the help message Default value: false. Possible values: {true, false}"
                ),
            ),
            ToolInput(
                tag="inp",
                input_type=String(optional=True),
                prefix="--input",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-I) BAM/SAM/CRAM file containing reads This argument may be specified 0 or more times. Default value: null. "
                ),
            ),
            ToolInput(
                tag="intervalExclusionPadding",
                input_type=Int(optional=True),
                prefix="--interval-exclusion-padding",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-ixp)  Amount of padding (in bp) to add to each interval you are excluding.  Default value: 0. "
                ),
            ),
            ToolInput(
                tag="intervalMergingRule",
                input_type=Boolean(optional=True),
                prefix="--interval-merging-rule",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-imr)  Interval merging rule for abutting intervals  Default value: ALL. Possible values: {ALL, OVERLAPPING_ONLY} "
                ),
            ),
            ToolInput(
                tag="intervalPadding",
                input_type=Boolean(optional=True),
                prefix="--interval-padding",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="(-ip) Default value: 0."),
            ),
            ToolInput(
                tag="intervalSetRule",
                input_type=Boolean(optional=True),
                prefix="--interval-set-rule",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-isr)  Set merging approach to use for combining interval inputs  Default value: UNION. Possible values: {UNION, INTERSECTION} "
                ),
            ),
            ToolInput(
                tag="intervals",
                input_type=String(optional=True),
                prefix="--intervals",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-L) One or more genomic intervals over which to operate This argument may be specified 0 or more times. Default value: null. "
                ),
            ),
            ToolInput(
                tag="lenient",
                input_type=Boolean(optional=True),
                prefix="--lenient",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-LE) Lenient processing of VCF files Default value: false. Possible values: {true, false}"
                ),
            ),
            ToolInput(
                tag="quiet",
                input_type=Boolean(optional=True),
                prefix="--QUIET",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Whether to suppress job-summary info on System.err. Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="readFilter",
                input_type=String(optional=True),
                prefix="--read-filter",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-RF) Read filters to be applied before analysis This argument may be specified 0 or more times. Default value: null. Possible Values: {AlignmentAgreesWithHeaderReadFilter, AllowAllReadsReadFilter, AmbiguousBaseReadFilter, CigarContainsNoNOperator, FirstOfPairReadFilter, FragmentLengthReadFilter, GoodCigarReadFilter, HasReadGroupReadFilter, IntervalOverlapReadFilter, LibraryReadFilter, MappedReadFilter, MappingQualityAvailableReadFilter, MappingQualityNotZeroReadFilter, MappingQualityReadFilter, MatchingBasesAndQualsReadFilter, MateDifferentStrandReadFilter, MateOnSameContigOrNoMappedMateReadFilter, MateUnmappedAndUnmappedReadFilter, MetricsReadFilter, NonChimericOriginalAlignmentReadFilter, NonZeroFragmentLengthReadFilter, NonZeroReferenceLengthAlignmentReadFilter, NotDuplicateReadFilter, NotOpticalDuplicateReadFilter, NotSecondaryAlignmentReadFilter, NotSupplementaryAlignmentReadFilter, OverclippedReadFilter, PairedReadFilter, PassesVendorQualityCheckReadFilter, PlatformReadFilter, PlatformUnitReadFilter, PrimaryLineReadFilter, ProperlyPairedReadFilter, ReadGroupBlackListReadFilter, ReadGroupReadFilter, ReadLengthEqualsCigarLengthReadFilter, ReadLengthReadFilter, ReadNameReadFilter, ReadStrandFilter, SampleReadFilter, SecondOfPairReadFilter, SeqIsStoredReadFilter, SoftClippedReadFilter, ValidAlignmentEndReadFilter, ValidAlignmentStartReadFilter, WellformedReadFilter}"
                ),
            ),
            ToolInput(
                tag="readIndex",
                input_type=String(optional=True),
                prefix="--read-index",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-read-index)  Indices to use for the read inputs. If specified, an index must be provided for every read input and in the same order as the read inputs. If this argument is not specified, the path to the index for each input will be inferred automatically.  This argument may be specified 0 or more times. Default value: null. "
                ),
            ),
            ToolInput(
                tag="readLimit",
                input_type=Int(optional=True),
                prefix="--read-limit",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-read-limit)  Maximum number of reads to encode in a tensor, for 2D models only.  Default value: 128. "
                ),
            ),
            ToolInput(
                tag="readValidationStringency",
                input_type=Boolean(optional=True),
                prefix="--read-validation-stringency",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-VS)  Validation stringency for all SAM/BAM/CRAM/SRA files read by this program.  The default stringency value SILENT can improve performance when processing a BAM file in which variable-length data (read, qualities, tags) do not otherwise need to be decoded.  Default value: SILENT. Possible values: {STRICT, LENIENT, SILENT} "
                ),
            ),
            ToolInput(
                tag="secondsBetweenProgressUpdates",
                input_type=Double(optional=True),
                prefix="--seconds-between-progress-updates",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-seconds-between-progress-updates)  Output traversal statistics every time this many seconds elapse  Default value: 10.0. "
                ),
            ),
            ToolInput(
                tag="sequenceDictionary",
                input_type=String(optional=True),
                prefix="--sequence-dictionary",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-sequence-dictionary)  Use the given sequence dictionary as the master/canonical sequence dictionary.  Must be a .dict file.  Default value: null. "
                ),
            ),
            ToolInput(
                tag="sitesOnlyVcfOutput",
                input_type=Boolean(optional=True),
                prefix="--sites-only-vcf-output",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" If true, don't emit genotype fields when writing vcf file output.  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="tensorType",
                input_type=Boolean(optional=True),
                prefix="--tensor-type",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-tensor-type)  Name of the tensors to generate, reference for 1D reference tensors and read_tensor for 2D tensors.  Default value: reference. Possible values: { reference ( 1 Hot encoding of a reference sequence. ) read_tensor (Read tensor are 3D tensors spanning aligned reads, sites and channels. The maximum number of reads is a hyper-parameter typically set to 128. There are 15 channels in the read tensor. They correspond to the reference sequence data (4), read sequence data (4), insertions and deletions (2) read flags (4) and mapping quality (1).) } "
                ),
            ),
            ToolInput(
                tag="tmpDir",
                input_type=Boolean(optional=True),
                prefix="--tmp-dir",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Temp directory to use. Default value: null."
                ),
            ),
            ToolInput(
                tag="useJdkDeflater",
                input_type=Boolean(optional=True),
                prefix="--use-jdk-deflater",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-jdk-deflater)  Whether to use the JdkDeflater (as opposed to IntelDeflater)  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="useJdkInflater",
                input_type=Boolean(optional=True),
                prefix="--use-jdk-inflater",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-jdk-inflater)  Whether to use the JdkInflater (as opposed to IntelInflater)  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="verbosity",
                input_type=Boolean(optional=True),
                prefix="--verbosity",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-verbosity)  Control verbosity of logging.  Default value: INFO. Possible values: {ERROR, WARNING, INFO, DEBUG} "
                ),
            ),
            ToolInput(
                tag="version",
                input_type=Boolean(optional=True),
                prefix="--version",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="display the version number for this tool Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="weights",
                input_type=String(optional=True),
                prefix="--weights",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-weights) Keras model HD5 file with neural net weights. Default value: null."
                ),
            ),
            ToolInput(
                tag="windowSize",
                input_type=Int(optional=True),
                prefix="--window-size",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-window-size)  Neural Net input window size  Default value: 128. "
                ),
            ),
            ToolInput(
                tag="disableAvxCheck",
                input_type=Boolean(optional=True),
                prefix="--disable-avx-check",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-disable-avx-check)  If set, no check will be made for AVX support.  Use only if you have installed a pre-1.6 TensorFlow build.   Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="disableToolDefaultReadFilters",
                input_type=Boolean(optional=True),
                prefix="--disable-tool-default-read-filters",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-disable-tool-default-read-filters)  Disable all tool default read filters (WARNING: many tools will not function correctly without their default read filters on)  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="inferenceBatchSize",
                input_type=Int(optional=True),
                prefix="--inference-batch-size",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-inference-batch-size)  Size of batches for python to do inference on.  Default value: 256. "
                ),
            ),
            ToolInput(
                tag="infoAnnotationKeys",
                input_type=String(optional=True),
                prefix="--info-annotation-keys",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-info-annotation-keys)  The VCF info fields to send to python.  This should only be changed if a new model has been trained which expects the annotations provided here.  This argument may be specified 0 or more times. Default value: [MQ, DP, SOR, FS, QD, MQRankSum, ReadPosRankSum]. "
                ),
            ),
            ToolInput(
                tag="interOpThreads",
                input_type=Int(optional=True),
                prefix="--inter-op-threads",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-inter-op-threads)  Number of inter-op parallelism threads to use for Tensorflow  Default value: 0. "
                ),
            ),
            ToolInput(
                tag="intraOpThreads",
                input_type=Int(optional=True),
                prefix="--intra-op-threads",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-intra-op-threads)  Number of intra-op parallelism threads to use for Tensorflow  Default value: 0. "
                ),
            ),
            ToolInput(
                tag="outputTensorDir",
                input_type=String(optional=True),
                prefix="--output-tensor-dir",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-output-tensor-dir)  Optional directory where tensors can be saved for debugging or visualization.  Default value: . "
                ),
            ),
            ToolInput(
                tag="showhidden",
                input_type=Boolean(optional=True),
                prefix="--showHidden",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-showHidden)  display hidden arguments  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="transferBatchSize",
                input_type=Int(optional=True),
                prefix="--transfer-batch-size",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-transfer-batch-size)  Size of data to queue for python streaming.  Default value: 512. "
                ),
            ),
            ToolInput(
                tag="ambigFilterBases",
                input_type=Int(optional=True),
                prefix="--ambig-filter-bases",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Threshold number of ambiguous bases. If null, uses threshold fraction; otherwise, overrides threshold fraction.  Default value: null.  Cannot be used in conjuction with argument(s) maxAmbiguousBaseFraction"
                ),
            ),
            ToolInput(
                tag="ambigFilterFrac",
                input_type=Double(optional=True),
                prefix="--ambig-filter-frac",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Threshold fraction of ambiguous bases Default value: 0.05. Cannot be used in conjuction with argument(s) maxAmbiguousBases"
                ),
            ),
            ToolInput(
                tag="maxFragmentLength",
                input_type=Boolean(optional=True),
                prefix="--max-fragment-length",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="Default value: 1000000."),
            ),
            ToolInput(
                tag="minFragmentLength",
                input_type=Boolean(optional=True),
                prefix="--min-fragment-length",
                separate_value_from_prefix=True,
                doc=InputDocumentation(doc="Default value: 0."),
            ),
            ToolInput(
                tag="keepIntervals",
                input_type=String(optional=True),
                prefix="--keep-intervals",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="One or more genomic intervals to keep This argument must be specified at least once. Required. "
                ),
            ),
            ToolInput(
                tag="library",
                input_type=String(optional=True),
                prefix="--library",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-library) Name of the library to keep This argument must be specified at least once. Required."
                ),
            ),
            ToolInput(
                tag="maximumMappingQuality",
                input_type=Int(optional=True),
                prefix="--maximum-mapping-quality",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Maximum mapping quality to keep (inclusive)  Default value: null. "
                ),
            ),
            ToolInput(
                tag="minimumMappingQuality",
                input_type=Int(optional=True),
                prefix="--minimum-mapping-quality",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Minimum mapping quality to keep (inclusive)  Default value: 10. "
                ),
            ),
            ToolInput(
                tag="dontRequireSoftClipsBothEnds",
                input_type=Boolean(optional=True),
                prefix="--dont-require-soft-clips-both-ends",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Allow a read to be filtered out based on having only 1 soft-clipped block. By default, both ends must have a soft-clipped block, setting this flag requires only 1 soft-clipped block  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="filterTooShort",
                input_type=Int(optional=True),
                prefix="--filter-too-short",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Minimum number of aligned bases Default value: 30."
                ),
            ),
            ToolInput(
                tag="platformFilterName",
                input_type=Boolean(optional=True),
                prefix="--platform-filter-name",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="This argument must be specified at least once. Required."
                ),
            ),
            ToolInput(
                tag="blackListedLanes",
                input_type=String(optional=True),
                prefix="--black-listed-lanes",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Platform unit (PU) to filter out This argument must be specified at least once. Required."
                ),
            ),
            ToolInput(
                tag="readGroupBlackList",
                input_type=Boolean(optional=True),
                prefix="--read-group-black-list",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="This argument may be specified 0 or more times. Default value: [ID:ArtificialHaplotypeRG, ID:ArtificialHaplotype]. "
                ),
            ),
            ToolInput(
                tag="keepReadGroup",
                input_type=String(optional=True),
                prefix="--keep-read-group",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="The name of the read group to keep Required."
                ),
            ),
            ToolInput(
                tag="maxReadLength",
                input_type=Int(optional=True),
                prefix="--max-read-length",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Keep only reads with length at most equal to the specified value Required."
                ),
            ),
            ToolInput(
                tag="minReadLength",
                input_type=Int(optional=True),
                prefix="--min-read-length",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Keep only reads with length at least equal to the specified value Default value: 1."
                ),
            ),
            ToolInput(
                tag="readName",
                input_type=String(optional=True),
                prefix="--read-name",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="Keep only reads with this read name Required."
                ),
            ),
            ToolInput(
                tag="keepReverseStrandOnly",
                input_type=Boolean(optional=True),
                prefix="--keep-reverse-strand-only",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Keep only reads on the reverse strand  Required. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="sample",
                input_type=String(optional=True),
                prefix="--sample",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc="(-sample) The name of the sample(s) to keep, filtering out all others This argument must be specified at least once. Required. "
                ),
            ),
            ToolInput(
                tag="invertSoftClipRatioFilter",
                input_type=Boolean(optional=True),
                prefix="--invert-soft-clip-ratio-filter",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Inverts the results from this filter, causing all variants that would pass to fail and visa-versa.  Default value: false. Possible values: {true, false} "
                ),
            ),
            ToolInput(
                tag="softClippedLeadingTrailingRatio",
                input_type=Double(optional=True),
                prefix="--soft-clipped-leading-trailing-ratio",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Threshold ratio of soft clipped bases (leading / trailing the cigar string) to total bases in read for read to be filtered.  Default value: null.  Cannot be used in conjuction with argument(s) minimumSoftClippedRatio"
                ),
            ),
            ToolInput(
                tag="softClippedRatioThreshold",
                input_type=Double(optional=True),
                prefix="--soft-clipped-ratio-threshold",
                separate_value_from_prefix=True,
                doc=InputDocumentation(
                    doc=" Threshold ratio of soft clipped bases (anywhere in the cigar string) to total bases in read for read to be filtered.  Default value: null.  Cannot be used in conjuction with argument(s) minimumLeadingTrailingSoftClippedRatio"
                ),
            ),
        ]

    def outputs(self):
        return [ToolOutput("out", VcfTabix, glob=InputSelector("outputFilename"))]

    def metadata(self):
        return ToolMetadata(
            contributors=["Michael Franklin"],
            dateCreated=datetime(2020, 5, 18),
            dateUpdated=datetime(2020, 5, 18),
            documentation="""USAGE: CNNScoreVariants [arguments]
            
Annotate a VCF with scores from a Convolutional Neural Network (CNN).The CNN determines a Log Odds Score for each
variant.Pre-trained models (1D or 2D) are specified via the architecture argument.1D models will look at the reference
sequence and variant annotations.2D models look at aligned reads, reference sequence, and variant annotations.2D models
require a BAM file as input as well as the tensor-type argument to be set.
""",
        )
