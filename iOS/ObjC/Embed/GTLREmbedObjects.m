// NOTE: This file was generated by the ServiceGenerator.

// ----------------------------------------------------------------------------
// API:
//   Embed API (embed/v1)
// Description:
//   Provides the ability to embed various Bloombox data in 3rd party apps and
//   websites.

#import "GTLREmbedObjects.h"

// ----------------------------------------------------------------------------
// Constants

// GTLREmbed.EmbeddedMenuStyle
NSString * const kGTLREmbed_EmbeddedMenuStyle_MasterDetail = @"MASTER_DETAIL";
NSString * const kGTLREmbed_EmbeddedMenuStyle_MasterOnly   = @"MASTER_ONLY";

// ----------------------------------------------------------------------------
//
//   GTLREmbed_DedData
//

@implementation GTLREmbed_DedData
@dynamic environment, link;
@end


// ----------------------------------------------------------------------------
//
//   GTLREmbed_DedViewSpec
//

@implementation GTLREmbed_DedViewSpec
@dynamic location, partner, payload, script, style;
@end
