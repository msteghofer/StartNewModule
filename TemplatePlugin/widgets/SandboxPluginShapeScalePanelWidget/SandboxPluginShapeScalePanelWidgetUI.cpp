// -*- C++ -*- generated by wxGlade 0.6.3 on Fri Oct 10 10:20:18 2008

#include "SandboxPluginShapeScalePanelWidgetUI.h"

// begin wxGlade: ::extracode

// end wxGlade

SandboxPluginShapeScalePanelWidgetUI::SandboxPluginShapeScalePanelWidgetUI(wxWindow* parent, int id, const wxPoint& pos, const wxSize& size, long style):
    wxScrolledWindow(parent, id, pos, size, wxTAB_TRAVERSAL)
{
    // begin wxGlade: SandboxPluginShapeScalePanelWidgetUI::SandboxPluginShapeScalePanelWidgetUI
    m_GlobalVolumeClosing_staticbox = new wxStaticBox(this, -1, wxT("Scale shape"));
    m_labelScale = new wxStaticText(this, wxID_ANY, wxT("Scale"));
    m_textScale = new wxTextCtrl(this, wxID_ANY, wxEmptyString);
    m_btnScale = new wxButton(this, wxID_BTN_SCALE, wxT("Apply"));

    set_properties();
    do_layout();
    // end wxGlade
}


void SandboxPluginShapeScalePanelWidgetUI::set_properties()
{
    // begin wxGlade: SandboxPluginShapeScalePanelWidgetUI::set_properties
    SetScrollRate(10, 10);
    // end wxGlade
}


void SandboxPluginShapeScalePanelWidgetUI::do_layout()
{
    // begin wxGlade: SandboxPluginShapeScalePanelWidgetUI::do_layout
    wxBoxSizer* GlobalSizer = new wxBoxSizer(wxVERTICAL);
    wxStaticBoxSizer* m_GlobalVolumeClosing = new wxStaticBoxSizer(m_GlobalVolumeClosing_staticbox, wxVERTICAL);
    wxBoxSizer* sizer_5_copy_2_copy_copy_copy = new wxBoxSizer(wxHORIZONTAL);
    sizer_5_copy_2_copy_copy_copy->Add(m_labelScale, 1, 0, 0);
    sizer_5_copy_2_copy_copy_copy->Add(m_textScale, 0, 0, 0);
    m_GlobalVolumeClosing->Add(sizer_5_copy_2_copy_copy_copy, 0, wxEXPAND, 0);
    m_GlobalVolumeClosing->Add(m_btnScale, 0, wxALL|wxEXPAND, 5);
    GlobalSizer->Add(m_GlobalVolumeClosing, 1, wxALL|wxEXPAND, 5);
    SetSizer(GlobalSizer);
    GlobalSizer->Fit(this);
    // end wxGlade
}

