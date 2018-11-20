from lsst.obs.superbit.ingest import SuperbitParseTask
config.parse.retarget(SuperbitParseTask)

config.parse.translation = {'dataType':'OBSTYPE',
                            'expTime':'EXPTIME',
                            'filter':'FILTER',
                            'visit':'FRAMEID'}

config.parse.translators = {'dateObs':'translateDate',
                            'taiObs':'translateDate'}

config.register.visit = ['visit']

config.register.unique = ['visit', 'filter']

config.register.columns = {'visit':'int',
                           'filter':'text',
                           'dataType':'text',
                           'expTime':'double',
                           'dateObs':'text',
                           'taiObs':'text'}
