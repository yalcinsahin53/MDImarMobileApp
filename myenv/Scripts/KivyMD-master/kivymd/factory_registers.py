"""
Register KivyMD widgets to use without import.
"""

from kivy.factory import Factory

register = Factory.register
register("MDSegmentedButton", module="kivymd.uix.segmentedbutton")
register("MDSegmentedButtonItem", module="kivymd.uix.segmentedbutton")
register("MDSegmentButtonIcon", module="kivymd.uix.segmentedbutton")
register("MDSegmentButtonLabel", module="kivymd.uix.segmentedbutton")
register("MDScrollView", module="kivymd.uix.scrollview")
register("MDRecycleView", module="kivymd.uix.recycleview")
register("MDResponsiveLayout", module="kivymd.uix.responsivelayout")
register("MDSliverAppbar", module="kivymd.uix.sliverappbar")
register("MDSliverAppbarContent", module="kivymd.uix.sliverappbar")
register("MDSliverAppbarHeader", module="kivymd.uix.sliverappbar")
register("MDNavigationRailItem", module="kivymd.uix.navigationrail")
register("MDNavigationRail", module="kivymd.uix.navigationrail")
register("MDNavigationRailFabButton", module="kivymd.uix.navigationrail")
register("MDNavigationRailMenuButton", module="kivymd.uix.navigationrail")
register("MDNavigationRailItemIcon", module="kivymd.uix.navigationrail")
register("MDNavigationRailItemLabel", module="kivymd.uix.navigationrail")
register("MDSwiper", module="kivymd.uix.swiper")
register("MDWidget", module="kivymd.uix.widget")
register("MDFloatLayout", module="kivymd.uix.floatlayout")
register("MDAnchorLayout", module="kivymd.uix.anchorlayout")
register("MDScreen", module="kivymd.uix.screen")
register("MDScreenManager", module="kivymd.uix.screenmanager")
register("MDRecycleGridLayout", module="kivymd.uix.recyclegridlayout")
register("MDBoxLayout", module="kivymd.uix.boxlayout")
register("MDRelativeLayout", module="kivymd.uix.relativelayout")
register("MDGridLayout", module="kivymd.uix.gridlayout")
register("MDStackLayout", module="kivymd.uix.stacklayout")
register("MDExpansionPanel", module="kivymd.uix.expansionpanel")
register("MDExpansionPanelHeader", module="kivymd.uix.expansionpanel")
register("MDExpansionPanelContent", module="kivymd.uix.expansionpanel")
register("FitImage", module="kivymd.uix.fitimage")
register("MDBackdrop", module="kivymd.uix.backdrop")
register("MDTooltip", module="kivymd.uix.tooltip")
register("MDTooltipPlain", module="kivymd.uix.tooltip")
register("MDTooltipRich", module="kivymd.uix.tooltip")
register("MDTooltipRichActionButton", module="kivymd.uix.tooltip")
register("MDTooltipRichSubhead", module="kivymd.uix.tooltip")
register("MDTooltipRichSupportingText", module="kivymd.uix.tooltip")
register("MDBottomSheet", module="kivymd.uix.bottomsheet")
register("MDBottomSheetDragHandle", module="kivymd.uix.bottomsheet")
register("MDBottomSheetDragHandleButton", module="kivymd.uix.bottomsheet")
register("MDBottomSheetDragHandleTitle", module="kivymd.uix.bottomsheet")
register("MDNavigationBar", module="kivymd.uix.navigationbar")
register("MDNavigationItem", module="kivymd.uix.navigationbar")
register("MDNavigationItemLabel", module="kivymd.uix.navigationbar")
register("MDNavigationItemIcon", module="kivymd.uix.navigationbar")
register("MDToggleButton", module="kivymd.uix.behaviors.toggle_behavior")
register("MDButton", module="kivymd.uix.button")
register("MDButtonText", module="kivymd.uix.button")
register("MDButtonIcon", module="kivymd.uix.button")
register("MDFabButton", module="kivymd.uix.button")
register("MDIconButton", module="kivymd.uix.button")
register("MDExtendedFabButton", module="kivymd.uix.button")
register("MDExtendedFabButtonIcon", module="kivymd.uix.button")
register("MDExtendedFabButtonText", module="kivymd.uix.button")
register("MDCard", module="kivymd.uix.card")
register("MDDivider", module="kivymd.uix.divider")
register("MDChip", module="kivymd.uix.chip")
register("MDChipLeadingAvatar", module="kivymd.uix.chip")
register("MDChipLeadingIcon", module="kivymd.uix.chip")
register("MDChipTrailingIcon", module="kivymd.uix.chip")
register("MDChipText", module="kivymd.uix.chip")
register("MDSmartTile", module="kivymd.uix.imagelist")
register("MDSmartTileOverlayContainer", module="kivymd.uix.imagelist")
register("MDSmartTileImage", module="kivymd.uix.imagelist")
register("MDLabel", module="kivymd.uix.label")
register("MDIcon", module="kivymd.uix.label")
register("MDBadge", module="kivymd.uix.badge")
register("MDList", module="kivymd.uix.list")
register("MDListItem", module="kivymd.uix.list")
register("MDListItemHeadlineText", module="kivymd.uix.list")
register("MDListItemSupportingText", module="kivymd.uix.list")
register("MDListItemTrailingSupportingText", module="kivymd.uix.list")
register("MDListItemLeadingIcon", module="kivymd.uix.list")
register("MDListItemTrailingIcon", module="kivymd.uix.list")
register("MDListItemTrailingCheckbox", module="kivymd.uix.list")
register("MDListItemTertiaryText", module="kivymd.uix.list")
register("HoverBehavior", module="kivymd.uix.behaviors.hover_behavior")
register("FocusBehavior", module="kivymd.uix.behaviors.focus_behavior")
register("MagicBehavior", module="kivymd.uix.behaviors.magic_behavior")
register("MDNavigationDrawer", module="kivymd.uix.navigationdrawer")
register("MDNavigationLayout", module="kivymd.uix.navigationdrawer")
register("MDNavigationDrawerMenu", module="kivymd.uix.navigationdrawer")
register("MDNavigationDrawerItem", module="kivymd.uix.navigationdrawer")
register(
    "MDNavigationDrawerItemLeadingIcon", module="kivymd.uix.navigationdrawer"
)
register(
    "MDNavigationDrawerItemTrailingText", module="kivymd.uix.navigationdrawer"
)
register("MDNavigationDrawerHeader", module="kivymd.uix.navigationdrawer")
register("MDNavigationDrawerItemText", module="kivymd.uix.navigationdrawer")
register("MDNavigationDrawerLabel", module="kivymd.uix.navigationdrawer")
register("MDNavigationDrawerDivider", module="kivymd.uix.navigationdrawer")
register("MDScrollViewRefreshLayout", module="kivymd.uix.refreshlayout")
register("MDCheckbox", module="kivymd.uix.selectioncontrol")
register("MDSwitch", module="kivymd.uix.selectioncontrol")
register("MDSlider", module="kivymd.uix.slider")
register("MDCircularProgressIndicator", module="kivymd.uix.progressindicator")
register("MDLinearProgressIndicator", module="kivymd.uix.progressindicator")
register("MDTabsPrimary", module="kivymd.uix.tab")
register("MDTabsSecondary", module="kivymd.uix.tab")
register("MDTabsItem", module="kivymd.uix.tab")
register("MDTabsItemSecondary", module="kivymd.uix.tab")
register("MDTabsBadge", module="kivymd.uix.tab")
register("MDTabsItemIcon", module="kivymd.uix.tab")
register("MDTabsItemText", module="kivymd.uix.tab")
register("MDTabsCarousel", module="kivymd.uix.tab")
register("MDTextField", module="kivymd.uix.textfield")
register("MDTextFieldHelperText", module="kivymd.uix.textfield")
register("MDTextFieldMaxLengthText", module="kivymd.uix.textfield")
register("MDTextFieldHintText", module="kivymd.uix.textfield")
register("MDTextFieldLeadingIcon", module="kivymd.uix.textfield")
register("MDTextFieldTrailingIcon", module="kivymd.uix.textfield")
register("MDTopAppBarTrailingButtonContainer", module="kivymd.uix.appbar")
register("MDTopAppBarLeadingButtonContainer", module="kivymd.uix.appbar")
register("MDFabBottomAppBarButton", module="kivymd.uix.appbar")
register("MDActionBottomAppBarButton", module="kivymd.uix.appbar")
register("MDTopAppBarTitle", module="kivymd.uix.appbar")
register("MDTopAppBar", module="kivymd.uix.appbar")
register("MDBottomAppBar", module="kivymd.uix.appbar")
register("MDActionTopAppBarButton", module="kivymd.uix.appbar")
register("MDDropDownItem", module="kivymd.uix.dropdownitem")
register("MDDropDownItemText", module="kivymd.uix.dropdownitem")
register("MDCircularLayout", module="kivymd.uix.circularlayout")
register("MDHeroFrom", module="kivymd.uix.hero")
register("MDHeroTo", module="kivymd.uix.hero")