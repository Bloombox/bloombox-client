// NOTE: This file was generated by the ServiceGenerator.

// ----------------------------------------------------------------------------
// API:
//   Embed API (embed/v1)
// Description:
//   Provides the ability to embed various Bloombox data in 3rd party apps and
//   websites.

#import "GTLREmbedQuery.h"

#import "GTLREmbedObjects.h"

// ----------------------------------------------------------------------------
// Constants

// style
NSString * const kGTLREmbedStyleMasterDetail = @"MASTER_DETAIL";
NSString * const kGTLREmbedStyleMasterOnly   = @"MASTER_ONLY";

// ----------------------------------------------------------------------------
// Query Classes
//

@implementation GTLREmbedQuery

@dynamic fields;

@end

@implementation GTLREmbedQuery_Data

@dynamic location, partner;

+ (instancetype)queryWithPartner:(NSString *)partner
                        location:(NSString *)location {
  NSArray *pathParams = @[
    @"location", @"partner"
  ];
  NSString *pathURITemplate = @"{partner}/{location}/data";
  GTLREmbedQuery_Data *query =
    [[self alloc] initWithPathURITemplate:pathURITemplate
                               HTTPMethod:nil
                       pathParameterNames:pathParams];
  query.partner = partner;
  query.location = location;
  query.expectedObjectClass = [GTLREmbed_DedData class];
  query.loggingName = @"embed.data";
  return query;
}

@end

@implementation GTLREmbedQuery_View

@dynamic location, partner, style;

+ (instancetype)queryWithPartner:(NSString *)partner
                        location:(NSString *)location
                           style:(NSString *)style {
  NSArray *pathParams = @[
    @"location", @"partner", @"style"
  ];
  NSString *pathURITemplate = @"{partner}/{location}/view/{style}";
  GTLREmbedQuery_View *query =
    [[self alloc] initWithPathURITemplate:pathURITemplate
                               HTTPMethod:nil
                       pathParameterNames:pathParams];
  query.partner = partner;
  query.location = location;
  query.style = style;
  query.expectedObjectClass = [GTLREmbed_DedViewSpec class];
  query.loggingName = @"embed.view";
  return query;
}

@end