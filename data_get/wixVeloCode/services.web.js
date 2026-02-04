import { wixEventsV2 } from 'wix-events.v2';
import { posts } from 'wix-blog-backend';
import wixData from 'wix-data';

const SERVICE_FIND_EVENTS = 'REPLACE_ME_EVENTS_SERVICE_FUNCTION';
const SERVICE_FIND_BLOG_POSTS = 'REPLACE_ME_BLOG_POSTS_SERVICE_FUNCTION';
const SERVICE_FIND_COLLECTION = 'REPLACE_ME_COLLECTION_SERVICE_FUNCTION';
const SERVICE_FIND_BLOG_CATEGORIES =
	'REPLACE_ME_BLOG_CATEGORIES_SERVICE_FUNCTION';
const SERVICE_FIND_BLOG_TAGS = 'REPLACE_ME_BLOG_TAGS_SERVICE_FUNCTION';
const SERVICE_FIND_MEMBERS = 'REPLACE_ME_MEMBERS_SERVICE_FUNCTION';

/**
 * https://dev.wix.com/docs/velo/apis/wix-events-v2/wix-events-v2/query-events
 */
export async function yourFindEventsServiceFunction() {
	let allEvents = [];

	let query = wixEventsV2.queryEvents().ne('status', 'CANCELED').limit(50);

	try {
		let results = await query.find();

		// Loop through all pages of results
		while (results.items.length > 0) {
			allEvents = allEvents.concat(results.items); // Add the current page's items to the list

			if (results.hasNext()) {
				results = await results.next(); // Get the next page
			} else {
				break; // Exit loop if no more pages
			}
		}

		return allEvents;
	} catch (error) {
		console.error(
			`❌ [${SERVICE_FIND_EVENTS}]: Error querying events from Wix Events:`,
			error
		);
		throw new Error('Failed to retrieve all events from Wix Events V2');
	}
}

/**
 * https://dev.wix.com/docs/velo/apis/wix-blog-backend/posts/query-posts
 */
export async function yourFindBlogPostsServiceFunction(options) {
	let allPosts = [];
	let query = posts.queryPosts(options).limit(50); // Start the query with a limit

	try {
		let results = await query.find();

		// Loop through all pages of results
		while (results.items.length > 0) {
			allPosts = allPosts.concat(results.items); // Add the current page's items to the list

			if (results.hasNext()) {
				results = await results.next(); // Get the next page
			} else {
				break; // Exit loop if no more pages
			}
		}

		return allPosts;
	} catch (error) {
		console.error(
			`❌ [${SERVICE_FIND_BLOG_POSTS}]: Error querying post:`,
			error
		);
		throw new Error('Failed to retrieve posts.');
	}
}

/**
 * https://dev.wix.com/docs/velo/apis/wix-blog-backend/categories/query-categories
 */
export async function yourFindBlogCategoriesServiceFunction() {
	try {
		const results = await categories.queryCategories().find();
		const items = results.items;

		return items;
	} catch (error) {
		console.error(
			`❌ [${SERVICE_FIND_BLOG_CATEGORIES}]: Error querying blog categories:`,
			error
		);
		throw new Error('Failed to retrieve blog categories.');
	}
}

/**
 * https://dev.wix.com/docs/velo/apis/wix-blog-backend/tags/get-tag-by-slug
 */
export async function yourFindBlogTagsServiceFunction() {
	try {
		const queryTagsResults = await tags.queryTags().find();
		const items = queryTagsResults.items;

		return items;
	} catch (error) {
		console.error(
			`❌ [${SERVICE_FIND_BLOG_TAGS}]: Error querying blog tags:`,
			error
		);
		throw new Error('Failed to retrieve blog categories.');
	}
}

/**
 * https://dev.wix.com/docs/velo/apis/wix-data/query
 */
export async function yourFindCollectionServiceFunction(collectionId) {
	try {
		const retrievedCollection = await wixData.query(collectionId).find();
		return retrievedCollection;
	} catch (error) {
		console.error(
			`❌ [${SERVICE_FIND_COLLECTION}]: Error querying collection:`,
			error
		);
		throw new Error('Failed to retrieve collection.');
	}
}

/**
 * https://dev.wix.com/docs/velo/apis/wix-members-v2/members/query-members
 */
export async function yourFindMembersServiceFunction(options) {
	try {
		const siteMembers = await members.queryMembers(options).find();

		return siteMembers;
	} catch (error) {
		console.error(
			`❌ [${SERVICE_FIND_MEMBERS}]: Error querying members:`,
			error
		);
		throw new Error('Failed to retrieve members.');
	}
}
