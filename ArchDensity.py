from qgis.PyQt.QtCore import QCoreApplication
from qgis.core import (QgsProcessing, QgsProcessingAlgorithm,
                       QgsProcessingParameterFeatureSource,
                       QgsProcessingParameterVectorDestination)


import processing

class ArchDensity(QgsProcessingAlgorithm):
    INPUT = 'INPUT'
    LAYERS = 'LAYERS'
    OUTPUT = 'OUTPUT'

    def __init__(self):
        super().__init__()

    def tr(self, string):

        return QCoreApplication.translate('Processing', string)


    def name(self):
        return "ArchDensity"

    def displayName(self):
        return "Archeo Density"


    def createInstance(self):
        return type(self)()


    def shortHelpString(self):

        return self.tr("Export the total in m2 of archaeological features and their density within the excavation area. In case of invalid geometries the algorithm will not calculate them in the final count and therefore the total percentage may be lower than the reality")


    def initAlgorithm(self, config=None):

        self.addParameter(
            QgsProcessingParameterFeatureSource(
                self.INPUT,
                'Excavation Area',
                [QgsProcessing.TypeVectorAnyGeometry]
            )
        )

        self.addParameter(
            QgsProcessingParameterFeatureSource(
                self.LAYERS,
                'Archaeology Area',
                [QgsProcessing.TypeVectorAnyGeometry]
            )
        )

        self.addParameter(
            QgsProcessingParameterVectorDestination (
                self.OUTPUT,
                'Density'
            )
        )

    def processAlgorithm(self, parameters, context, feedback):
        outputFile = self.parameterAsOutputLayer(parameters, self.OUTPUT, context)

        overlap_layer = processing.run("qgis:calculatevectoroverlaps",
            {
                'INPUT': parameters['INPUT'],
                'LAYERS': parameters['LAYERS'],
                'OUTPUT': outputFile
            },
            is_child_algorithm=True,
            context=context,
            feedback=feedback
        )['OUTPUT']

        return {self.OUTPUT : overlap_layer}
