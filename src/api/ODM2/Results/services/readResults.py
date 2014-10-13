import sys
import os



from ... import serviceBase
from ..model import *

__author__ = 'Jacob'

class readResults(serviceBase):
    """queries to tables contained in Results schema"""



    """
    TimeSeriesResults
    """
    def getAllTimeSeriesResults(self):
        """Select all on TimeSeriesResults

        :return TimeSeriesResults Objects:
            :type list:
        """
        return self._session.query(Timeseriesresult).all()

    def getTimeSeriesResultsByResultId(self, resultId):
        """Select by resultID on ResultID

        :param resultId:
            :type Integer:
        :return return matching Timeseriesresult Object filtered by resultId
        """

        try:
            return self._session.query(Timeseriesresult).filter_by(ResultID=resultId).one()
        except:
            return None

    def getTimeSeriesResultsbyCode(self, timeSeriesCode):
        """Select by time
        """
        pass


    """
    TimeSeriesResultValues
    """
    def getAllTimeSeriesValues(self):
        """Select all on TimeSeriesResults

        :return TimeSeriesResultsValue Objects:
            :type list:
        """
        return self._session.query(Timeseriesresultvalue).all()

    def getTimeSeriesValuesByResultId(self, resultId):
        """Select by resultId

        :param timeSeriesId:
            :type Integer:
        :return return matching Timeseriesresultvalue Object filtered by resultId:
            :type Timeseriesresultvalue:
        """
        try:
            return self._session.query(Timeseriesresultvalue).filter_by(ResultID=resultId).all()
        except:
            return None

    def getTimeSeriesValuesByCode(self, timeSeriesCode):
        """

        :param timeSeriesCode:
        :return:
        """
        pass

    def getTimeSeriesValuesByTime(self, resultid, starttime, endtime=None):

        # set end = start if it is None
        endtime = starttime if not endtime else endtime

        try:
            return self._session.query(Timeseriesresultvalue).filter_by(ResultID=resultid) \
                                                      .filter(Timeseriesresultvalue.ValueDateTime >= starttime) \
                                                      .filter(Timeseriesresultvalue.ValueDateTime <= endtime) \
                                                      .order_by(Timeseriesresultvalue.ValueDateTime).all()
        except:
            return None