/*
* Copyright (c) 2009,
* Computational Image and Simulation Technologies in Biomedicine (CISTIB),
* Universitat Pompeu Fabra (UPF), Barcelona, Spain. All rights reserved.
* See license.txt file for details.
*/

#include "TemplatePluginTemplProcessor.h"

#include <string>
#include <iostream>

#include "coreReportExceptionMacros.h"
#include "coreDataEntity.h"
#include "coreDataEntityHelper.h"
#include "coreDataEntityHelper.txx"
#include "coreKernel.h"
#include "coreVTKPolyDataHolder.h"
#include "coreVTKImageDataHolder.h"

#include "vtkSmartPointer.h"

TemplatePlugin::TemplProcessor::TemplProcessor( )
{
	SetName( "TemplProcessor" );
	
	BaseProcessor::SetNumberOfInputs( INPUTS_NUMBER );
	GetInputPort(INPUT_0)->SetName(  "Input Image" );
	GetInputPort(INPUT_0)->SetDataEntityType( Core::ImageTypeId);
	GetInputPort(INPUT_1)->SetName(  "Input Surface" );
	GetInputPort(INPUT_1)->SetDataEntityType( Core::SurfaceMeshTypeId);
	BaseProcessor::SetNumberOfOutputs( OUTPUTS_NUMBER );
	
}

TemplatePlugin::TemplProcessor::~TemplProcessor()
{
}

void TemplatePlugin::TemplProcessor::Update()
{
	try
	{
		// Get the first image
		ImageType::Pointer itkInputImage;
		GetProcessingData(INPUT_0,
			itkInputImage);

		Core::vtkPolyDataPtr vtkInput;
		GetProcessingData(INPUT_1,
			vtkInput );
			
		Core::vtkImageDataPtr vtkInputImage;
		GetProcessingData(INPUT_0,
			vtkInputImage );
			

		// Set state to processing (dialog box)
		SetState( Core::Runtime::APP_STATE_PROCESSING );

		// here goes the filter or the functions that determine the processor
		// the output should go in the update functions
		
		// Set the output to the output of this processor
		UpdateOutput( 0 ,itkInputImage, "TemplProcessorImage");	
		UpdateOutput(1, vtkInput, "TemplProcessorSurface");
		UpdateOutput(2, vtkInputImage, "TemplProcessorImageVTK");
	}
	catch(...)
	{
		// Throw the exception again to be catched by the Widget and
		// show a message box with the error message
		SetState( Core::Runtime::APP_STATE_IDLE );

		throw;
	}

	SetState( Core::Runtime::APP_STATE_IDLE );

}